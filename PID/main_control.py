from PID import pid_control
import time
import MySQLdb
from socket import socket, SOCK_STREAM, AF_INET
from threading import Thread
from json import dumps
from json import loads


class Tcp_server(Thread):
    def __init__(self, cclient):
        super().__init__()
        self.cclient = cclient

    def run(self):
        """
        主要功能
        1.接收气压传感器数据
        2.接收陀螺仪传感器器数据
        3.转发数据给pid
        4.接收pid反馈数据
        5.将各项数据存储至Mysql
        """
        data = self.cclient.recv(1024)
        my_dict = loads(data.decode('utf-8'))
        return my_dict


class Main_Control:
    def __init__(self):
        self.pid = pid_control.PID_control()
        self.db = MySQLdb.connect(host='192.168.1.103', user='root', passwd='201411', db='data_save')
        self.db0 = self.db.cursor()
        self.server = socket(family=AF_INET, type=SOCK_STREAM)
        self.set_point = 0.0

    def dealwith_data(self, set_point):
        """
        数据格式应为
        {
            'name':'Pressure_Sensor',
            'value':0.01,
        }
        :param set_point:
        :return:
        """
        self.set_point = set_point
        self.server.bind(('192.168.1.2', 5566))
        self.server.listen(512)
        client, addr = self.server.accept()
        data = Tcp_server(client).start()
        if data['name'] == 'Pressure_Sensor':
            value = data['value']
            output, num = self.pid.loop(self.set_point, value)
            # output输出给阀
            self.into_sql(value, 1)
        elif data['name'] == 'Angle_Sensor':
            avalue = data['value']
            self.into_sql(avalue, 2)

    def into_sql(self, data, x):
        if x == 1:
            sql = 'INSERT INTO PressureSensor(id,p_value)VALUES(NULL,' + str(data) + ');'
            self.db0.execute(sql)
            self.db.commit()
            self.db.close()
        if x == 2:
            sql = 'INSERT INTO AngleSensor(id,a_value)VALUES(NULL,' + str(data) + ');'
            self.db0.execute(sql)
            self.db.commit()
            self.db.close()

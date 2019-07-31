from PID import pid_control
import time
import MySQLdb
from socket import socket, SOCK_STREAM, AF_INET

class Main_Control:
    def __init__(self):
        self.pid = pid_control.PID_control()
        self.db = MySQLdb.connect(host='192.168.1.103', user='root', passwd='201411', db='pyqt_schema')
        self.server = socket(family=AF_INET, type=SOCK_STREAM)

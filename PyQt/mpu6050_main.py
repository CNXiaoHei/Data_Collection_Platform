from mpu6050 import Mpu6050
from threading import Thread

class Datasend(Thread):
    def __init__(self, cclient):
        super().__init__()
        self.cclient = cclient
        self.adr1 = 0x43
        self.adr2 = 0x45
        self.adr3 = 0x47
        self.adr4 = 0x3b
        self.adr5 = 0x3d
        self.adr6 = 0x3f

    def run(self):
        mpu = Mpu6050()
        gyro_xout = mpu.read_word_2c(self.adr1)
        gyro_yout = mpu.read_word_2c(self.adr2)
        gyro_zout = mpu.read_word_2c(self.adr3)
        accel_xout = mpu.read_word_2c(self.adr4)
        accel_yout = mpu.read_word_2c(self.adr5)
        accel_zout = mpu.read_word_2c(self.adr6)
        accel_xout_scaled = accel_xout / 16384.0
        accel_yout_scaled = accel_yout / 16384.0
        accel_zout_scaled = accel_zout / 16384.0
        x_rotation = mpu.get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
        y_rotation = mpu.get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
        dicts = {'gyro_xout':gyro_xout, 'gyro_yout':gyro_yout, 'gyro_zout':gyro_zout, 'accel_xout_scaled':accel_xout_scaled, 'accel_yout_scaled':accel_yout_scaled, 'accek_zout_scaled':accel_zout_scaled, 'x_rotation':x_rotation, 'y_rotation':y_rotation}
        return dicts

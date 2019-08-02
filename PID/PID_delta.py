class PID_delta:
    def __init__(self, P=0.2, I=0.0, D=0.0):
        self.Kp = P
        self.Ki = I
        self.Kd = D
        # 增量误差
        self.error = 0
        self.error1 = 0
        self.error2 = 0
        # 位置误差
        self.perror = 0
        self.perror1 = 0
        self.ierror = 0
        self.i = 0   # 计数
        self.j = 0
        self.Actualvalue = 0

    def updata(self, feedback, setpoint):
        self.i += 1
        self.error = setpoint - feedback
        if self.i > 3:
            output = self.Kp * (self.error - self.error1) + self.Ki * self.error + self.Kd * (self.error - 2 * self.error1 + self.error2)
        self.error2 = self.error1
        self.error1 = self.error
        self.Actualvalue += output
        return self.Actualvalue

    def realize(self, feedback, setpoint):
        self.j += 1
        self.perror = setpoint - feedback
        self.ierror += self.perror
        if self.ierror > 10:
            self.ierror = 10
        elif self.ierror < -10:
            self.ierror = -10
        if self.j > 3:
            output = self.Kp * self.perror + self.Ki * self.ierror + self.Kd * (self.perror - self.perror1)
        self.perror1 = self.perror
        return output

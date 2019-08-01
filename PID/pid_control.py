import PID.PID as PID

class PID_control:
    def __init__(self, P=0.2, I=0.0, D=0.0, L=50):
        self.pid = PID.PID(P, I, D)
        self.pid.SetPoint = 0.0
        self.pid.setSampleTime(0.01)
        self.feedback = 0.0
        self.i = 0
        self.current_time = 0         # 数据类型要修改
        self.last_time = 0            # 数据类型要修改

    def loop(self, set_point, current_time):
        self.i += 1
        self.current_time = current_time
        self.pid.update(self.feedback, self.current_time, self.last_time)
        output = self.pid.output
        if self.pid.SetPoint > 0:
            # self.feedback = feedback
            pass
        if self.i > 9:
            self.pid.SetPoint = set_point
        self.last_time = self.current_time
        return output, self.i
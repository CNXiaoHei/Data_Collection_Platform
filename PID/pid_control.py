import PID.PID as PID

class PID_control:
    def __init__(self, P=0.2, I=0.0, D=0.0, L=50):
        self.pid = PID.PID(P, I, D)
        self.pid.SetPoint = 0.0
        self.pid.setSampleTime(0.01)
        self.feedback = 0.0
        self.i = 0

    def loop(self, setpoint):
        self.i += 1
        self.pid.update(self.feedback)
        output = self.pid.output
        if self.pid.SetPoint > 0:
            self.feedback += (output - (1/self.i))
        if self.i > 9:
            self.pid.SetPoint = setpoint
        return self.feedback, self.i

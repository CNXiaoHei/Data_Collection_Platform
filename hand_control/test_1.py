import AD_DA_main as adda
import PID


class Test_one:
    def __init__(self, setpoint, filename):
        self.pid = PID.PID(3.5,0,0)
        self.Setpiont = setpoint
        self.pid.SetPoint = setpoint
        self.adda = adda.AD_DA_Transfer()
        self.filename = filename
        self.create_file(filename)
        self.feedback = 0.0

    def create_file(self, filename):
        f = open(filename+'.csv', 'w')
        f.writelines('feedback,pid_out\n')
        f.close()

    def get_value(self):
        value = self.adda.get_value()
        self.feedback = (value['AD7']-1)/0.4*100

    def write_value(self, value):
        self.adda.da_value(value, 0.1)

    def rrr(self, value):
        self.write_value(value)
        self.get_value()
        print(self.feedback)
        
    def wula(self):
        self.get_value()
        feedback = self.feedback
        print(feedback)
        self.pid.update(feedback)
        pid_out = self.pid.output
        print(pid_out)
        print(self.pid.SetPoint)
        if pid_out<0:
            self.write_value(0.04)
        elif pid_out>100:
            self.write_value(3)
        else:
            self.write_value((pid_out)*0.02)
        f = open(self.filename+'.csv', 'a')
        csv = str(feedback)+','+str(pid_out)+'\n'
        f.writelines(csv)
        f.close()


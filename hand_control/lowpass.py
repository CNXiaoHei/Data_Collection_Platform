import matplotlib.pyplot as plt

class Lowpass:
    def __init__(self):
        self.y_current = 0
        self.y_last = 0
        self.u_current = 0
        self.u_last = 0

    def lowpass(self, input):
        self.u_last = self.u_current
        self.u_current = input
        self.y_last = self.y_current
        self.y_current = 0.9391*self.y_last+0.03046*(self.u_current+self.u_last)

# 测试低通滤波器
def main():
    data = []
    filter_data = []
    t = 0
    tt = []
    f = open(r'C:\Users\a4419\Desktop\data1029.csv', 'r')   #读取本地数据
    for line in f.readlines():
        list1 = line[0:-2]
        list2 = list1.split(',')
        data.append(eval(list2[0]))
        tt.append(t)
        t += 0.01
    f.close()
    lowpass = Lowpass()
    for i in range(2005):
        if i<5:
            lowpass.lowpass(0)
        else:
            lowpass.lowpass(data[i-5])
        filter_data.append(lowpass.y_current)
    plt.plot(tt, data)
    plt.plot(tt, filter_data[0:2000], color='red')
    plt.show()

main()

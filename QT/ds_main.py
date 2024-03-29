#-*-coding:utf-8-*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import numpy as np
from data_save import Ui_MainWindow

import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class My_Figure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(My_Figure, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)

    def plotsin(self):
        self.axes0 = self.fig.add_subplot(111)
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2*np.pi*t)
        self.axes0.plot(t, s)

    def plotcos(self):
        self.axes1 = self.fig.add_subplot(111)
        t = np.arange(0.0, 3.0, 0.01)
        s = np.cos(2*np.pi*t)
        self.axes1.plot(t.s)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('数据采集系统')
        self.setMinimumSize(0, 0)
        self.F = My_Figure(width=3, height=2, dpi=100)
        self.plotcos()
        self.gridlayout = QGridLayout(self.groupBox)
        self.gridlayout.addWidget(self.F, 0, 1)
        self.plotother()

    def plotcos(self):
        t = np.arange(0.0, 5.0, 0.01)
        s = np.cos(2*np.pi*t)
        self.F.axes.plot(t, s)

    def plotother(self):
        F1 = My_Figure(width=5, height=4, dpi=100)
        F1.fig.suptitle('figure')
        F1.axes1 = F1.fig.add_subplot(221)
        x = np.arange(0, 50)
        y = np.random.rand(50)
        F1.axes1.hist(y,bins=50)
        F1.axes1.plot(x, y)
        F1.axes1.bar(x, y)
        F1.axes1.set_title('hist')
        F1.axes2 = F1.fig.add_subplot(222)
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
        F1.axes2.plot(x, y)
        F1.axes2.set_title("line")
        # 散点图
        F1.axes3 = F1.fig.add_subplot(223)
        F1.axes3.scatter(np.random.rand(20), np.random.rand(20))
        F1.axes3.set_title("scatter")
        # 折线图
        F1.axes4 = F1.fig.add_subplot(224)
        x = np.arange(0, 5, 0.1)
        F1.axes4.plot(x, np.sin(x), x, np.cos(x))
        F1.axes4.set_title("sincos")
        self.gridlayout.addWidget(F1, 0, 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

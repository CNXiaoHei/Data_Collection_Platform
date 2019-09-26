# -*-coding:utf-8-*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import numpy as np

import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from s import *

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
        self.axes1.plot(t,s)

class Main_system(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main_system, self).__init__(parent)
        self.setupUi(self)
        self.F = My_Figure(width=3,height=2,dpi=100)
        self.gridlayout = QGridLayout(self.groupBox)
        self.gridlayout.addWidget(self.F,0,1)
        self.set_btn.clicked.connect(self.set_pressvalue)
        self.reset_btn.clicked.connect(self.reset_pressvalue)
        self.lcd_p.display(10.1)
        self.lcd_x.display(10)
        self.lcd_y.display(10)
        self.lcd_z.display(10)
        self.F.plotcos()

    def set_pressvalue(self):
        a = self.lineEdit.text()      # a为str类型


    def reset_pressvalue(self):
        self.lineEdit.setText('0')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ms = Main_system()
    ms.show()
    sys.exit(app.exec())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '界面.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(659, 431)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(180, 0, 461, 371))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(30, 30, 411, 321))
        self.widget.setObjectName("widget")
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 11, 161, 182))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(self.widget1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.set_btn = QtWidgets.QPushButton(self.splitter)
        self.set_btn.setObjectName("pushButton")

        self.reset_btn = QtWidgets.QPushButton(self.splitter)
        self.reset_btn.setObjectName("pushButton_2")

        self.verticalLayout.addWidget(self.splitter)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.lcd_p = QtWidgets.QLCDNumber(self.widget1)
        self.lcd_p.setObjectName("lcdNumber")
        self.lcd_p.setDigitCount(5)
        self.lcd_p.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_p.setSmallDecimalPoint(True)

        self.gridLayout.addWidget(self.lcd_p, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.lcd_x = QtWidgets.QLCDNumber(self.widget1)
        self.lcd_x.setObjectName("lcdNumber_2")
        self.lcd_x.setDigitCount(5)
        self.lcd_x.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.gridLayout.addWidget(self.lcd_x, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.lcd_y = QtWidgets.QLCDNumber(self.widget1)
        self.lcd_y.setObjectName("lcdNumber_3")
        self.lcd_y.setDigitCount(5)
        self.lcd_y.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.gridLayout.addWidget(self.lcd_y, 2, 1, 1, 1)

        self.lcd_z = QtWidgets.QLCDNumber(self.widget1)
        self.lcd_z.setObjectName("lcdNumber_4")
        self.lcd_z.setDigitCount(5)
        self.lcd_z.setSegmentStyle(QtWidgets.QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcd_z, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "气压值曲线"))
        self.label.setText(_translate("MainWindow", "输入气压值："))
        self.set_btn.setText(_translate("MainWindow", "确定"))
        self.reset_btn.setText(_translate("MainWindow", "重置"))
        self.label_2.setText(_translate("MainWindow", "实时气压值："))
        self.label_3.setText(_translate("MainWindow", "X:"))
        self.label_4.setText(_translate("MainWindow", "Y:"))
        self.label_5.setText(_translate("MainWindow", "Z:"))

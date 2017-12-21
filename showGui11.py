# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiV5.ui'
#
# Created: Tue Apr 19 17:51:42 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

import sys
import random
import string
import time
#import pigpio # http://abyz.co.uk/rpi/pigpio/python.html
import re #for text parsing
from PySide import QtCore, QtGui

currentMax = 0
RPM = 0
Ctmp = 0
Mtmp = 0
Code = 0
Vlt = 0
Min = 0
Amps = 0
iteration = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 330, 61, 31))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(460, 20, 61, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.progressBar = QtGui.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_4.addWidget(self.progressBar)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 20, 441, 231))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setProperty("value", 52.0)
        self.lcdNumber.setProperty("intValue", 52)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 0, 61, 16))
        self.label_6.setObjectName("label_6")
        self.layoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(520, 20, 61, 231))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_11 = QtGui.QLabel(self.layoutWidget_2)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.progressBar_2 = QtGui.QProgressBar(self.layoutWidget_2)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_5.addWidget(self.progressBar_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 270, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(120, 660, 55, 16))
        self.label_14.setObjectName("label_14")
        self.Current_LCD_3 = QtGui.QLCDNumber(self.centralwidget)
        self.Current_LCD_3.setGeometry(QtCore.QRect(10, 270, 211, 39))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.Current_LCD_3.setFont(font)
        self.Current_LCD_3.setObjectName("Current_LCD_3")
        self.RPM_LCD_3 = QtGui.QLCDNumber(self.centralwidget)
        self.RPM_LCD_3.setGeometry(QtCore.QRect(230, 270, 221, 39))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.RPM_LCD_3.setFont(font)
        self.RPM_LCD_3.setProperty("intValue", 0)
        self.RPM_LCD_3.setObjectName("RPM_LCD_3")
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(430, 660, 36, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(90, 250, 111, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(340, 250, 61, 16))
        self.label_17.setObjectName("label_17")
        self.Current_LCD_2 = QtGui.QLCDNumber(self.centralwidget)
        self.Current_LCD_2.setGeometry(QtCore.QRect(10, 330, 211, 39))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.Current_LCD_2.setFont(font)
        self.Current_LCD_2.setObjectName("Current_LCD_2")
        self.RPM_LCD_2 = QtGui.QLCDNumber(self.centralwidget)
        self.RPM_LCD_2.setGeometry(QtCore.QRect(230, 330, 221, 39))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.RPM_LCD_2.setFont(font)
        self.RPM_LCD_2.setProperty("intValue", 0)
        self.RPM_LCD_2.setObjectName("RPM_LCD_2")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 370, 131, 16))
        self.label_4.setObjectName("label_4")
        self.Battery_Bar = QtGui.QProgressBar(self.centralwidget)
        self.Battery_Bar.setGeometry(QtCore.QRect(11, 389, 561, 41))
        self.Battery_Bar.setProperty("value", 24)
        self.Battery_Bar.setObjectName("Battery_Bar")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 310, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(340, 310, 61, 16))
        self.label_13.setObjectName("label_13")
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(460, 300, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_10.setObjectName("label_10")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 241, 141))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("binghamton-university-bearcats-logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 598, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       #Rfresh Gui 
        self._update_timer1 = QtCore.QTimer()
        self._update_timer1.timeout.connect(self.update_label)
        self._update_timer1.start(500) # milliseconds


    def updateUi(self):

        self.Current_LCD_2.display(currentMax) #Peak Current
        self.Current_LCD_3().display(Min) #Min Voltage
        self.RPM_LCD_3().display(Amps) #Current
        self.RPM_LCD_2().display(Vlt) #Voltage
        self.Battery_Bar.setValue(50) #Battery Bar
        self.label_7.setText("Error Code:" + str(Code)) #Error Code
        #self._update_timer = QtCore.QTimer()
        #self._update_timer.timeout.connect(self.update_label)
        #self._update_timer.start(1000) # milliseconds

    def update_label(self):
        inputFile = open('log.txt','r')
        rawText = inputFile.read()
        wordArray = rawText.split(" ")
        inputFile.close()
        self.lcdNumber.display(int(wordArray[7])) #Velocity
        self.Current_LCD_3.display(int(wordArray[3])) #Peak Current
        self.Current_LCD_2.display(int(wordArray[15])) #Min Voltage
        self.RPM_LCD_3.display(int(wordArray[5])) #Current
        self.RPM_LCD_2.display(int(wordArray[13])) #Voltage
        #self.Battery_Bar.setValue(50) #Battery Bar
        self.progressBar.setValue(int(wordArray[11])) #Motor Temp
        self.progressBar_2.setValue(int(wordArray[9])) #Controller Temp
        self.label_7.setText("Error Code:" + wordArray[17]) #Error Code
        self.label_10.setText(str(int(self.label_10.text()) + 1))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Dbug", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "M Temp", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setFormat(QtGui.QApplication.translate("MainWindow", "%v%", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Velocity", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "C Temp", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar_2.setFormat(QtGui.QApplication.translate("MainWindow", "%v%", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Error Code: 0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Min Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "Peak Current", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "Current", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Battery Level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Min Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))

class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QtGui.QApplication(sys.argv)
mySW = ControlMainWindow()
mySW.show()


sys.exit(app.exec_())

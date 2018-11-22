# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alee3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Alee import Ui_OtherWindow
from Alee2 import Ui_CameraWindow
class Ui_HomeWindow(object):
    
     def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_OtherWindow()
        self.ui.setupUi(self.window)
        
        self.window.show()
     def openWindow2(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_CameraWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
     def setupUi(self,MainWindow):
        MainWindow.setObjectName("HomeWindow")
        MainWindow.resize(577, 510)
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-20, -2, 601, 621))
        self.frame.setStyleSheet("background-image:  url(\"./xxxxxx.png\"); background-repeat: n-repeat;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.HomeWindow = QtWidgets.QFrame(self.centralwidget)
        self.HomeWindow.setGeometry(QtCore.QRect(-1, 0, 581, 521))
        self.HomeWindow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HomeWindow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HomeWindow.setObjectName("HomeWindow")
        self.alionebtn = QtWidgets.QPushButton(self.HomeWindow)
        self.alionebtn.setGeometry(QtCore.QRect(10, 360, 261, 71))
        self.alionebtn.setStyleSheet("font: 12pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 73, 95);")
        self.alionebtn.setCheckable(False)
        self.alionebtn.setObjectName("alionebtn")
        self.alionebtn.clicked.connect(self.openWindow)
        self.frame_3 = QtWidgets.QFrame(self.HomeWindow)
        self.frame_3.setGeometry(QtCore.QRect(10, 20, 571, 71))
        self.frame_3.setStyleSheet("background-image:url(\"./face recognition title.png\");\n"
"background-repeat:no-repeat;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.alitwobtn = QtWidgets.QPushButton(self.HomeWindow)
        self.alitwobtn.setGeometry(QtCore.QRect(290, 360, 281, 71))
        self.alitwobtn.setStyleSheet("font: 12pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 73, 95);")
        self.alitwobtn.setCheckable(False)
        self.alitwobtn.setObjectName("alitwobtn")
        self.alitwobtn.clicked.connect(self.openWindow2)
        self.label = QtWidgets.QLabel(self.HomeWindow)
        self.label.setGeometry(QtCore.QRect(10, 100, 341, 16))
        self.label.setStyleSheet("font: 13pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.HomeWindow)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 421, 21))
        self.label_2.setStyleSheet("font: 11pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.HomeWindow)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 551, 31))
        self.label_3.setStyleSheet("font: 11pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.HomeWindow)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 481, 21))
        self.label_4.setStyleSheet("font: 11pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.HomeWindow)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 261, 31))
        self.label_5.setStyleSheet("font: 11pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

     def retranslateUi(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.alionebtn.setText(_translate("MainWindow", "Organize Your Data Artificially"))
        self.alitwobtn.setText(_translate("MainWindow", "Start Video And Recognize"))
        self.label.setText(_translate("MainWindow", "This Desktop Application is developed to:"))
        self.label_2.setText(_translate("MainWindow", "1. Organize Your Tangled Data Into An Intelligent Way"))
        self.label_3.setText(_translate("MainWindow", "2. Additionally, This Will Be Used In Hundreds Of Different Places To "))
        self.label_4.setText(_translate("MainWindow", "Recognize People Through Its Ability To Learn And Encode Face "))
        self.label_5.setText(_translate("MainWindow", "Artificially Using Machine Learning"))



import sys
app = QtWidgets.QApplication(sys.argv)
HomeWindow = QtWidgets.QMainWindow()
ui = Ui_HomeWindow()
ui.setupUi(HomeWindow)
HomeWindow.show()
sys.exit(app.exec_())


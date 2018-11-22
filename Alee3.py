# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alee3n.ui'
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

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("HomeWindow")
        MainWindow.resize(579, 506)
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-1, -1, 581, 511))
        self.frame_2.setStyleSheet("background-image:url(\"./xxxxxx.png\")\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 360, 262, 92))
        self.pushButton_3.setStyleSheet("background:transparent;\n"
"background-image:url(\"./organizeDataButton.png\");\n"
"\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openWindow)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 20, 571, 71))
        self.frame_3.setStyleSheet("background-image:url(\"./face_recognition_title.png\");\n"
"background-repeat:no-repeat;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
         
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 360, 262, 92))
        self.pushButton_4.setStyleSheet("background:transparent;\n"
"background-image:url(\"./videoButton.png\");\n"
"\n"
"")
        self.pushButton_4.setText("")
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.pushButton_4.clicked.connect(self.openWindow2)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 100, 351, 21))
        self.label.setStyleSheet("background:transparent;\n"
"font: 14pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 421, 21))
        self.label_2.setStyleSheet("background:transparent;\n"
"font: 12pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 551, 31))
        self.label_3.setStyleSheet("background:transparent;\n"
"font: 12pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 491, 21))
        self.label_4.setStyleSheet("background:transparent;\n"
"font: 12pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 261, 31))
        self.label_5.setStyleSheet("background:transparent;\n"
"font: 12pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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



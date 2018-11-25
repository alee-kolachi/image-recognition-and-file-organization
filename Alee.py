# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aleen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


#Author - Alee Kolachi

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import recognize_faces_in_pictures as rfip
import os,sys
class Ui_OtherWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("OtherWindow")
        MainWindow.resize(607, 500)
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-20, -10, 631, 511))
        self.frame.setStyleSheet("background-image:  url(\"./xxxxxx.png\"); background-repeat: n-repeat;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(18, 0, 611, 521))
        self.frame_2.setStyleSheet("background-image:url(\"./xxxxxx.png\");")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.please_wait = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(50, 350, 111, 31))
        self.please_wait.setGeometry(QtCore.QRect(110, 420,81 , 21))
        self.label_3.setAutoFillBackground(False)
        self.please_wait.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background:transparent;\n"
"font: 75 13pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.please_wait.setStyleSheet("background:transparent;\n"
"font: 75 10pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.please_wait.hide()
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.please_wait.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("label_3")
        self.please_wait.setObjectName("please_wait")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 280, 401, 31))
        self.lineEdit_2.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Microsoft YaHei UI\";\n"
"border-color: rgb(0, 83, 59);\n"
"padding-left: 7px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 280, 101, 31))
        self.pushButton_2.setStyleSheet("font: 12pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 73, 95);")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.getFolderName)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(50, 170, 101, 31))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background:transparent;\n"
"font: 75 13pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(230, 44, 131, 31))
        self.label_5.setStyleSheet("background:transparent;\n"
"font: 75 17pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 410, 141, 41))
        self.pushButton_3.setStyleSheet("font: 12pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 73, 95);")
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.compareBtn)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(50, 250, 101, 31))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background:transparent;\n"
"font: 75 13pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(7, 17, 601, 31))
        self.label_4.setStyleSheet("background:transparent;\n"
"font: 75 17pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(470, 200, 101, 31))
        self.pushButton.setStyleSheet("font: 12pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 73, 95);")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openFileNameDialog)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 350, 281, 31))
        self.lineEdit_4.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Microsoft YaHei UI\";\n"
"border-color: rgb(0, 83, 59);\n"
"padding-left: 7px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 200, 401, 31))
        self.lineEdit_3.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Microsoft YaHei UI\";\n"
"border-color: rgb(0, 83, 59);\n"
"padding-left: 7px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(20, 490, 461, 16))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("background:transparent;\n"
"font: 75 10pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 90, 491, 51))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("background:transparent;\n"
"font: 75 10pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setObjectName("label_7")
        self.openFolderButton = QtWidgets.QPushButton(self.frame_2)
        self.openFolderButton.setGeometry(QtCore.QRect(470, 350, 101, 31))
        self.openFolderButton.setStyleSheet("font: 11.6pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 73, 95);")
        self.openFolderButton.setCheckable(False)
        self.openFolderButton.setEnabled(False)
        self.openFolderButton.setObjectName("openFolderButton")
        self.openFolderButton.clicked.connect(self.getFolderPath)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", " Folder Name*"))
        self.please_wait.setText(_translate("MainWindow","please wait..."))
        self.pushButton_2.setText(_translate("MainWindow", "Folder Path"))
        self.label.setText(_translate("MainWindow", "Image Path*"))
        self.label_5.setText(_translate("MainWindow", "In This Age"))
        self.pushButton_3.setText(_translate("MainWindow", "Start Comparing"))
        self.label_2.setText(_translate("MainWindow", "Folder Path*"))
        self.label_4.setText(_translate("MainWindow", "Recognize And Organize Your Data Into A Meaningful Way"))
        self.pushButton.setText(_translate("MainWindow", "Image Path"))
        self.label_6.setText(_translate("MainWindow", "* Provide Image Path As Well As Folder Path And Folder Name In Fields Above"))
        self.label_7.setText(_translate("MainWindow", "1. In Image Path Field, Provide Image Path That You Want To Compare \n"
"2. In Folder Path, Provide Folder Path From Which The Image Would Be Compared.\n"
"3. In Folder Name, Provide Folder Name In Which Matched Images Will Be Saved."))
        self.openFolderButton.setText(_translate("MainWindow", "Open Folder"))

    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self.pushButton,"Choose the Image path", "","JPEG (*.jpg);;PNG (*.png)", options=options)
        if fileName:
            self.lineEdit_3.setText(fileName)
    def getFolderName(self):
        file = str(QFileDialog.getExistingDirectory(self.pushButton_2, "Select Directory"))
        self.lineEdit_2.setText(file)
    def compareBtn(self):
        _translate = QtCore.QCoreApplication.translate
        self.please_wait.show()
        self.enableOrDisable(True)
        rfip.method(self.lineEdit_3.text(),self.lineEdit_2.text(),self.lineEdit_4.text())
        self.enableOrDisable(False)
        self.label_6.setText(_translate("MainWindow", "Success: Your Images Organized Artificially."))
        self.openFolderButton.setEnabled(True)
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.hide()
    def enableOrDisable(self, b):
        #_translate = QtCore.QCoreApplication.translate
        if b == True:
            #self.compare.setText(_translate("MainWindow", ". . ."))
            self.please_wait.show()
            self.pushButton_3.setEnabled(False)
            
        elif b == False:
            self.pushButton_3.setDisabled(False)
            self.please_wait.hide()
            #self.compare.setText(_translate("MainWindow", "Start Comparing"))
    def getFolderPath(self):
        os.chdir(self.lineEdit_2.text()+"/"+self.lineEdit_4.text()+"/")
        directory=self.lineEdit_2.text()+"/"+self.lineEdit_4.text()
        filename,_ = QFileDialog.getOpenFileName(
           self.openFolderButton, 'Compared Images', os.getcwd(), "JPEG (*.jpg);;PNG (*.png)")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())

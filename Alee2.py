# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alee2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import face_recognition_webcam2 
class Ui_CameraWindow(object):
    def setupUi(self, CameraWindow):
        CameraWindow.setObjectName("CameraWindow")
        CameraWindow.resize(579, 502)
        CameraWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(CameraWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-20, -10, 601, 631))
        self.frame.setStyleSheet("background-image:  url(\"./xxxxxx.png\"); background-repeat: n-repeat;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-1, -1, 581, 511))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.folder_edit = QtWidgets.QLineEdit(self.frame_2)
        self.folder_edit.setGeometry(QtCore.QRect(20, 210, 401, 31))
        self.folder_edit.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Microsoft YaHei UI\";\n"
"border-color: rgb(0, 83, 59);\n"
"padding-left: 7px;")
        self.folder_edit.setText("")
        self.folder_edit.setObjectName("folder_edit")
        self.folderpath = QtWidgets.QPushButton(self.frame_2)
        self.folderpath.setGeometry(QtCore.QRect(440, 210, 101, 31))
        self.folderpath.setStyleSheet("font: 12pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 73, 95);")
        self.folderpath.setCheckable(False)
        self.folderpath.setObjectName("folderpath")
        self.folderpath.clicked.connect(self.getFolderName)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(210, 38, 111, 31))
        self.label_5.setStyleSheet("font: 75 16pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.comparefromfolder = QtWidgets.QPushButton(self.frame_2)
        self.comparefromfolder.setGeometry(QtCore.QRect(160, 350, 161, 61))
        self.comparefromfolder.setStyleSheet("font: 12pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 73, 95);")
        self.comparefromfolder.setCheckable(False)
        self.comparefromfolder.setObjectName("comparefromfolder")
        self.comparefromfolder.clicked.connect(self.openwebcam)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 101, 31))
        self.label_7.setGeometry(QtCore.QRect(10, 80, 451, 31))
        self.label_2.setAutoFillBackground(False)
        self.label_7.setAutoFillBackground(False)
        self.label_2.setStyleSheet("font: 75 13pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setStyleSheet("font: 75 10pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setObjectName("label_2")
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 521, 31))
        self.label_4.setStyleSheet("font: 75 16pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(20, 480, 241, 16))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("font: 75 10pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setObjectName("label_6")
        self.ip_address = QtWidgets.QLineEdit(self.frame_2)
        self.ip_address.setGeometry(QtCore.QRect(70, 300, 321, 30))
        self.ip_address.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Microsoft YaHei UI\";\n"
"border-color: rgb(0, 83, 59);\n"
"padding-left: 7px;")
        self.ip_address.setText("")
        self.ip_address.setObjectName("ip_address")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(40, 260, 391,31))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("font: 75 12pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("label_3")
        CameraWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CameraWindow)
        QtCore.QMetaObject.connectSlotsByName(CameraWindow)

    def retranslateUi(self, CameraWindow):
        _translate = QtCore.QCoreApplication.translate
        CameraWindow.setWindowTitle(_translate("CameraWindow", "MainWindow"))
        self.folderpath.setText(_translate("CameraWindow", "Folder Path"))
        self.label_5.setText(_translate("CameraWindow", "In This Age"))
        self.comparefromfolder.setText(_translate("CameraWindow", "Start Comparing"))
        self.label_2.setText(_translate("CameraWindow", "Folder Path*"))
        self.label_7.setText(_translate("CameraWindow", "=> In Folder Path, Provide Path Of The Folder Of Images to be Recognized."))
        self.label_4.setText(_translate("CameraWindow", "Use Your Cam And Recognize The World In A Fast Way"))
        self.label_6.setText(_translate("CameraWindow", "* Provide Folder Path In The Field Above"))
        self.label_3.setText(_translate("CameraWindow", "0 - Webcam / IP Address for Mobile Cam / Video Link*"))

    def getFolderName(self):
        file = str(QFileDialog.getExistingDirectory(self.folderpath, "Select Directory"))
        self.folder_edit.setText(file)
    def openwebcam(self):
        face_recognition_webcam2.method2(self.folder_edit.text(),self.ip_address.text())
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CameraWindow = QtWidgets.QMainWindow()
    ui = Ui_CameraWindow()
    ui.setupUi(CameraWindow)
    CameraWindow.show()
    sys.exit(app.exec_())


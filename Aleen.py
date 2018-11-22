# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alee.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import recognize_faces_in_pictures as rfip
# Load 
class Ui_OtherWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("OtherWindow")
        MainWindow.resize(579, 501)
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-20, -10, 601, 631))
        self.frame.setStyleSheet("background-image:  url(\"./xxxxxx.png\"); background-repeat: n-repeat;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.OtherWindow = QtWidgets.QFrame(self.centralwidget)
        self.OtherWindow.setGeometry(QtCore.QRect(-1, -1, 581, 511))
        self.OtherWindow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.OtherWindow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OtherWindow.setObjectName("OtherWindow")
        self.label_3 = QtWidgets.QLabel(self.OtherWindow)
        self.label_3.setGeometry(QtCore.QRect(20, 310, 111, 31))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("font: 75 13pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("label_3")
        self.unknown_edit = QtWidgets.QLineEdit(self.OtherWindow)
        self.unknown_edit.setGeometry(QtCore.QRect(20, 240, 401, 31))
        self.unknown_edit.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Microsoft YaHei UI\";\n"
"border-color: rgb(0, 83, 59);\n"
"padding-left: 7px;")
        self.unknown_edit.setText("")
        self.unknown_edit.setObjectName("unknown_edit")
        self.open_unknownimage = QtWidgets.QPushButton(self.OtherWindow)
        self.open_unknownimage.setGeometry(QtCore.QRect(440, 240, 101, 31))
        self.open_unknownimage.setStyleSheet("font: 12pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 73, 95);")
        self.open_unknownimage.setCheckable(False)
        self.open_unknownimage.setObjectName("open_unknownimage")
        self.open_unknownimage.clicked.connect(self.getFolderName)
        self.label = QtWidgets.QLabel(self.OtherWindow)
        self.label.setGeometry(QtCore.QRect(20, 120, 101, 31))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("font: 75 13pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.OtherWindow)
        self.label_5.setGeometry(QtCore.QRect(200, 50, 111, 31))
        self.label_5.setStyleSheet("font: 75 16pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.compare = QtWidgets.QPushButton(self.OtherWindow)
        self.compare.setGeometry(QtCore.QRect(200, 370, 141, 41))
        self.compare.setStyleSheet("font: 12pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 73, 95);")
        self.compare.setCheckable(False)
        self.compare.setObjectName("compare")
        self.compare.clicked.connect(self.compareBtn)
        self.label_2 = QtWidgets.QLabel(self.OtherWindow)
        self.label_2.setGeometry(QtCore.QRect(20, 210, 101, 31))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("font: 75 13pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.OtherWindow)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 551, 31))
        self.label_4.setStyleSheet("font: 75 16pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.open_knownimage = QtWidgets.QPushButton(self.OtherWindow)
        self.open_knownimage.setGeometry(QtCore.QRect(440, 150, 101, 31))
        self.open_knownimage.setStyleSheet("font: 12pt \"Microsoft JhengHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 73, 95);")
        self.open_knownimage.setCheckable(False)
        self.open_knownimage.setObjectName("open_knownimage")
        self.open_knownimage.clicked.connect(self.openFileNameDialog)
        self.folder_name = QtWidgets.QLineEdit(self.OtherWindow)
        self.folder_name.setGeometry(QtCore.QRect(140, 310, 281, 31))
        self.folder_name.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Microsoft YaHei UI\";\n"
"border-color: rgb(0, 83, 59);\n"
"padding-left: 7px;")
        self.folder_name.setObjectName("folder_name")
        self.known_edit = QtWidgets.QLineEdit(self.OtherWindow)
        self.known_edit.setGeometry(QtCore.QRect(20, 150, 401, 31))
        self.known_edit.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Microsoft YaHei UI\";\n"
"border-color: rgb(0, 83, 59);\n"
"padding-left: 7px;")
        self.known_edit.setText("")
        self.known_edit.setObjectName("known_edit")
        self.label_6 = QtWidgets.QLabel(self.OtherWindow)
        self.label_6.setGeometry(QtCore.QRect(20, 480, 461, 16))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("font: 75 10pt \"Microsoft New Tai Lue\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", " Folder Name*"))
        self.open_unknownimage.setText(_translate("MainWindow", "Folder Path"))
        self.label.setText(_translate("MainWindow", "Image Path*"))
        self.label_5.setText(_translate("MainWindow", "In This Age"))
        self.compare.setText(_translate("MainWindow", "Start Comparing"))
        self.label_2.setText(_translate("MainWindow", "Folder Path*"))
        self.label_4.setText(_translate("MainWindow", "Recognize And Organize Your Data Into A Meaningful Way"))
        self.open_knownimage.setText(_translate("MainWindow", "Image Path"))
        self.label_6.setText(_translate("MainWindow", "* Provide Image Path As Well As Folder Path And Folder Name In Fields Above"))
    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self.open_knownimage,"Choose the Image path", "","JPEG (*.jpg);;PNG (*.png)", options=options)
        if fileName:
            self.known_edit.setText(fileName)
    def getFolderName(self):
        file = str(QFileDialog.getExistingDirectory(self.open_unknownimage, "Select Directory"))
        self.unknown_edit.setText(file)
    def compareBtn(self):
        _translate = QtCore.QCoreApplication.translate
        self.enableOrDisable(True)
        rfip.method(self.known_edit.text(),self.unknown_edit.text(),self.folder_name.text())
        self.enableOrDisable(False)
        self.label_6.setText(_translate("MainWindow", "Success: Your Images Organized Artificially."))
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.hide()
    def enableOrDisable(self, b):
        #_translate = QtCore.QCoreApplication.translate
        if b == True:
            #self.compare.setText(_translate("MainWindow", ". . ."))
            self.compare.setEnabled(False)
            
        elif b == False:
            self.compare.setDisabled(False)
            #self.compare.setText(_translate("MainWindow", "Start Comparing"))
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())


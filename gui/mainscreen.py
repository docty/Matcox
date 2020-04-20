# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maticom.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from mcomp import main

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, message):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 586)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 70, 811, 331))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText(message)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 30, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.pushButton.setObjectName("pushButton")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 400, 801, 161))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 0, 791, 131))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 0, 791, 131))
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
		
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
		
        self.pushButton.clicked.connect(self.writeToBoard)
		
	

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Matcox"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Output"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "No Error"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Error Message"))

    

    def writeToBoard(self):
        text = self.textEdit.toPlainText()
        fy = open('./board.mc', 'w+')
        fy.writelines(text)
        fy = open('./board.mc', 'r')
        
        output = main.callRunner()
         
        if type(output).__name__ == 'str': 
            self.textEdit_2.setText(output)
        elif type(output).__name__ == 'NoneType': 
            self.textEdit_2.setText(output)
        else:
            n = ''
            for i in output:
                n = n+str(i)
            self.textEdit_2.setText(n)
        
        fy.close()
        
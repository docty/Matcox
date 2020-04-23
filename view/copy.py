# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homescreen.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 586)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.textBoard = QtWidgets.QTextEdit(self.centralwidget)
        self.textBoard.setGeometry(QtCore.QRect(0, 70, 811, 331))
        self.textBoard.setObjectName("textBoard")
        self.btnRun = QtWidgets.QPushButton(self.centralwidget)
        self.btnRun.setGeometry(QtCore.QRect(350, 30, 75, 23))
        self.btnRun.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.btnRun.setObjectName("btnRun")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 400, 801, 161))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textOutput = QtWidgets.QTextEdit(self.tab)
        self.textOutput.setGeometry(QtCore.QRect(0, 0, 791, 131))
        self.textOutput.setReadOnly(True)
        self.textOutput.setObjectName("textOutput")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textError = QtWidgets.QTextEdit(self.tab_2)
        self.textError.setGeometry(QtCore.QRect(0, 0, 791, 131))
        self.textError.setReadOnly(True)
        self.textError.setObjectName("textError")
        self.tabWidget.addTab(self.tab_2, "")
        self.labelDisplay = QtWidgets.QLabel(self.centralwidget)
        self.labelDisplay.setGeometry(QtCore.QRect(20, 20, 181, 31))
        self.labelDisplay.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.labelDisplay.setText("")
        self.labelDisplay.setObjectName("labelDisplay")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Matcox"))
        self.btnRun.setText(_translate("MainWindow", "Run"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Output"))
        self.textError.setPlaceholderText(_translate("MainWindow", "No Error"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Error Message"))

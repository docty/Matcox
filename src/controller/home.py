
import os
from PyQt5 import QtCore, QtWidgets
 
class HomeController:

    def __init__(self, window):
        self.window = window
        self.text = ""
       
    def registerEvents(self): 
        self.window.textBoard.setText(self.text)
        self.window.actionRun.triggered.connect(self.run)
        self.window.actionSave.triggered.connect(self.save)
        self.window.actionOpen.triggered.connect(self.open)  
         
        
    def run(self):
        os.system('matcox.exe '+ self.fileName) 

    def save(self):
        text = self.window.textBoard.toPlainText()
        name, check = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File', '', 'All Files (*);; Matcox Files (*.mx)')
        if check:
            fy = open(name, 'w+')
            fy.writelines(text)
            fy.close()

    def open(self):
        text = self.window.textBoard.toPlainText()
        name, check = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', '', 'All Files (*);; Matcox Files (*.mx)')
        if check:
            fy = open(name, 'r')
            self.fileName = name
            self.window.textBoard.setText(fy.read())  
            fy.close()
    

from mcomp import main
from PyQt5 import QtCore
from sympy import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import ast
class HomeController:



    def __init__(self, window):
        self.window = window
        ### Read Data From Board  ###
        file = open('./board.mc', 'r')
        self.text = file.read()
        file.close()
        ### Initialise Figure  ###
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
      
    def registerEvents(self):
        self.window.btnRun.clicked.connect(self.run)
        self.window.textBoard.setText(self.text)
        self.canvas.setMinimumSize(QtCore.QSize(268, 0))
        self.window.function.itemClicked.connect(self.itemFunction)
        self.window.textBoard.textChanged.connect(self.boardText)
         
        
    def run(self):
        ## Display panel at the bottom
        self.setInspectors()
        ## Read and Write On Board
        self.Read_Write_Board()
        ## Run Engine  ##
        self.runEngine()
        
        
    def boardText(self):
        print('gf')

    def itemFunction(self, item):
        functionName = '<span style="color:#2A7FFF">'+item.text().lower()+'</span>'
        functionName = functionName+'<span style="color:#FF7F55">{</span> <span style="font-style:italic">type here</span> <span style="color:#FF7F55">}</span/>'
        self.window.textBoard.setText(functionName)
        

    def display(self, value=''):
        mathText= r'$'+value+'$'
        self.canvas.deleteLater()
        self.figure.clear()
        self.canvas = FigureCanvas(self.figure)
        self.figure.suptitle(mathText)
        self.window.rightLayout.addWidget(self.canvas)
        self.window.textInspector.insertPlainText('Completed\n')

    ## Display Information On The Inspector Panel And Message Panel
    def setInspectors(self):
        self.window.textInspector.clear()
        self.window.textInspector.insertPlainText('Script is processing...\n')

    def Read_Write_Board(self):
        text = self.window.textBoard.toPlainText()
        fy = open('./board.mc', 'w+')
        fy.writelines(text)
        fy = open('./board.mc', 'r')
        fy.close()

    def runEngine(self):
        output = main.callRunner()
        filetype =  type(output).__name__
        
        if filetype == 'str' : 
            self.window.textMessage.setText(output.errorMessage)
        elif filetype == 'ErrorTask':
            self.window.textMessage.setText(output.errorMessage+'; '+ output.errorValue)
        else:
            n = ''
            for i in output:
                n = n+str(i)
            self.window.textMessage.setText(n)
            self.display(n)

        
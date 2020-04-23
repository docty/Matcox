
from mcomp import main
from sympy import *
import ast
class HomeController:



   
#self.window.labelDisplay.setText(str(self.equ))

    def __init__(self, window):
        ### Read Data From Board  ###
        file = open('./board.mc', 'r')
        self.text = file.read()
        file.close()
        self.window = window
        x = Symbol('x')
        init_printing()
        self.equ = Integral(sqrt(1/x), x)
        # code = ast.parse(str(self.equ), mode='eval')
        # self.data = eval(compile(code, '', mode='eval'))
         
        
     

    def registerEvents(self):
        self.window.btnRun.clicked.connect(self.writeToBoard)
        self.window.textBoard.setText(self.text)
         
        
         


    def writeToBoard(self):
        text = self.window.textBoard.toPlainText()
        fy = open('./board.mc', 'w+')
        fy.writelines(text)
        fy = open('./board.mc', 'r')
        
        output = main.callRunner()
        filetype =  type(output).__name__
        
        if filetype == 'str' : 
            self.window.textMessage.setText(output.errorMessage)
        elif filetype == 'ErrorTask':
            self.window.textMessage.setText(output.errorMessage+'; '+ output.errorValue)
        else:
            print(output)
            n = ''
            for i in output:
                n = n+str(i)
            self.window.textMessage.setText(n)
        
        fy.close()
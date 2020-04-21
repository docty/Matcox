
from mcomp import main

class HomeController:



   


    def __init__(self, window):
        ### Read Data From Board  ###
        file = open('./board.mc', 'r')
        self.text = file.read()
        file.close()
        self.window = window
        
        
     

    def registerEvents(self):
        self.window.btnRun.clicked.connect(self.writeToBoard)
        self.window.textBoard.setText(self.text)
         


    def writeToBoard(self):
        text = self.window.textBoard.toPlainText()
        fy = open('./board.mc', 'w+')
        fy.writelines(text)
        fy = open('./board.mc', 'r')
        
        output = main.callRunner()
         
        if type(output).__name__ == 'str': 
            self.window.textOutput.setText(output)
        elif type(output).__name__ == 'NoneType': 
            self.window.textOutput.setText(output)
        else:
            n = ''
            for i in output:
                n = n+str(i)
            self.window.textOutput.setText(n)
        
        fy.close()
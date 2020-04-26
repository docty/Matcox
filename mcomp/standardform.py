# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:18:37 2020

@author: Lenovo G50
"""
# Example base{25,10, 2}

class Standardform:
    
    def __init__(self, tokens):
        self.tokens = tokens 
        
    
    
    
    
    def getNextToken(self):
        self.pos += 1
        self.currentToken = self.tokens[self.pos]
        
        
        
        
    def results(self):
        number =  self.tokens[0].value
        index=0
        
        if self.tokens[0]._type == 'FLOAT':
            if number[0] == '0':
                number = number.replace('.', '')
                while number[0] == '0':
                    number = number[1 :]
                    index +=1
                counter = -index
            else:
                index  = number.index('.')
                number = number.replace('.', '')
                while number[-1] == '0':
                    number = number[:-1]
                counter = index-1
            result = number[0]+'.'+ number[1:]+'x10^{'+str(counter)+'}' 
        else:
            oldNumber = number
            while number[0] == '0':
                number = number[1 :]
                oldNumber = number
            while number[-1] == '0':
                number = number[:-1]
            result = number[0]+'.'+ number[1:]+'x10^{'+str(len(oldNumber)-1)+'}'
        return [result]
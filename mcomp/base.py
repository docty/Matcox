# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:18:37 2020

@author: Lenovo G50
"""
# Example base{25,10, 2}

class Base:
    
    def __init__(self, tokens):
        self.tokens = tokens 
         
        self.number = self.tokens[0].value
        self.sub = self.tokens[2].value
        self.base = self.tokens[4].value
    
    
    
    
    def getNextToken(self):
        self.pos += 1
        self.currentToken = self.tokens[self.pos]
        
        
        
        
    def results(self):
        a = int(self.number)
        b = int(self.base)
        data = []
        
        while int(a) > 0:
            reminder = int(a%b)
            a = int(a/b)
            data.append(reminder)
            
        return data[::-1]
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:29:56 2020

@author: Lenovo G50
"""


import sympy as sym



try:
    import constant
except ImportError:
    from . import constant

class Evaluate:
    
    def __init__(self, tokens):
        self.tokens = tokens 
        self.pos = 0
        self.currentToken = self.tokens[self.pos]
    
    
    
    
    def getNextToken(self):
        self.pos += 1
        self.currentToken = self.tokens[self.pos]
        
        
    
        
    def useCaseTest(self):
        data=''
        answer = 0
        for item in self.tokens:
                data = data+item.value
        i = 1
        while i <= len(self.tokens):
            if self.tokens[i-1]._type == 'INT':
                answer = sym.sympify(sym.sqrt(int(self.tokens[i-1].value)))
            i += 1
        
        return [answer]
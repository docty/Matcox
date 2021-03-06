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

class Solve:
    
    def __init__(self, tokens):
        self.tokens = tokens 
        self.pos = 0
        self.currentToken = self.tokens[self.pos]
    
    
    
    
    def getNextToken(self):
        self.pos += 1
        self.currentToken = self.tokens[self.pos]
        
        
    def expression(self):
         
        result = self.term()
         
        while self.currentToken._type in (constant.PLUS, constant.MINUS) :
            left = self.currentToken
            if left._type == constant.PLUS:
                self.getNextToken()
                result = result + self.term()
            elif left._type == constant.MINUS:
                self.getNextToken()
                result = result - self.term()
            
         
        return result
    
    
    def term(self):
        token  = self.currentToken
         
        if token._type == constant.INT:
            self.getNextToken()
            return int(token.value)
        
        
    def useCaseTest(self):
        data=''
        for item in self.tokens:
            data = data+item.value
        try:
            result = sym.sympify(str(data[:-1]))
            return [result]
        except sym.SympifyError:
            return ['Expression Is Incorrect']
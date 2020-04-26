# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:29:56 2020

@author: Lenovo G50
"""


import sympy as sym
import re


try:
    import constant
except ImportError:
    from . import constant

class Factorise:
    
    def __init__(self, tokens):
        self.tokens = tokens 
        self.pos = 0
        self.currentToken = self.tokens[self.pos]
    
    
    
    
    def getNextToken(self):
        self.pos += 1
        self.currentToken = self.tokens[self.pos]
        
        
        
        
    def results(self):
        
        output=''; data=''
        for item in self.tokens:
            output = output+item.value
        for item in output:
            if item in ['^', '+', '-', ')', '('] :
                if len(data) > 0 and data[-1] == ')': 
                    data =  data+item
                else:
                    data = data[:-1]
                    data =  data+item
            elif item.isalpha():
                data = data+item+'*'
            elif item.isdigit() :
                if len(data) > 0 and data[-1] == '*':
                    data = data[:-1]
                data = data+item+'*'
        if data[-1] == ')':
            data = data
        else:
            data = data[:-1]
        print(data)
        try:
            result = str(sym.factor(data))
            
            return [result.replace('*', '')]
        except sym.SympifyError:
            return ['Expression Is Incorrect']
        except sym.TypeError:
            return ['Cant\'t simplified ']
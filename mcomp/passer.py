# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:08:40 2020

@author: Lenovo G50
"""
import re
try:
    from reserved import res_word
    from error import ErrorTask
    import constant
    from  tokena import Token
except ImportError:
    from .reserved import res_word
    from .error import ErrorTask
    from . import constant
    from  .tokena import Token

class Passer:
    
    def __init__(self, tokens):
        self.tokens = tokens 
        self.pos = 0
        self.currentToken = self.tokens[self.pos]



  
        
    def grammar(self):
        
        resWord = self.checkReservedWord()
         
        if type(resWord).__name__ == 'ErrorTask':
          return None, resWord
        
        cury = self.checkCury()
         
        if type(cury).__name__ == 'ErrorTask':
            return None, cury
        
        if resWord == 'solve':
            
            express = self.checkExpression()
            if type(express).__name__ == 'ErrorTask':
                return None, express
            
        if resWord == 'base': 
            base = self.checkBase()
            if type(base).__name__ == 'ErrorTask':
                return None, base
            
        return self.tokens, None
        
                
    
    
    def getNextToken(self):
        self.pos += 1
        self.currentToken = self.tokens[self.pos]
        
        
    def checkReservedWord(self):
        
        if self.currentToken.value in res_word:
            currentValue = self.currentToken.value
            self.getNextToken()
            return  currentValue  
        else :
            return ErrorTask('Name does not exist',self.currentToken.value )
        
    def checkCury(self):
        
        if self.currentToken.value == '{':
            pass
        else:
            return ErrorTask('Missing', '{' )
        
        if self.tokens[-1].value == '}':
            pass
        else :
            return ErrorTask('Missing', '}' )
        
        self.getNextToken()
        return None
    
        
    
    def checkExpression(self):
        length = len(self.tokens) - 3
        i  = 1
        
        while i <= length:
            
            if self.currentToken.value in ['{', '}'] or re.match(r'[a-z]', self.currentToken.value) :
                return ErrorTask('Syntax Error',  self.currentToken.value)
            self.getNextToken()
            i = i+1

        return None
       
         
    
    
    def checkBase(self):
        if(self.currentToken._type == constant.INT):
            self.getNextToken()
        else:
            return ErrorTask('Number Missing')
        if(self.currentToken._type == constant.COMMA):
              self.getNextToken()
        else:
            return ErrorTask('Comma Missing', ',')
        if(self.currentToken._type == constant.INT):
            self.getNextToken()
        else:
            return ErrorTask('Number Missing')
        if(self.currentToken._type == constant.COMMA):
              self.getNextToken()
        else:
            return ErrorTask('Comma Missing', ',')
        if(self.currentToken._type == constant.INT):
            self.getNextToken()
        else:
            return ErrorTask('Number Missing')
        return 'pass'
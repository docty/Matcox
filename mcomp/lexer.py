"""
Created on Thu Apr 16 02:19:12 2020

@author: Henry Asiedu 

Lexer solve{x, 2x+8=10} 
"""
import re
try: 
    from error import ErrorTask
    from  tokena import Token
    from reserved  import res_word
    import constant
except ImportError:
    from .error import ErrorTask
    from  .tokena import Token
    from .reserved  import res_word
    from . import constant
 
class Lexer:
    
    def __init__(self, text):
       self.pos = 0 
       self.text = text
       self.currentChar = self.text[self.pos]
       
       
    def getNextChar(self):
        if self.pos == len(self.text)-1:
            self.currentChar = None
            return
        self.pos += 1
        self.currentChar = self.text[self.pos]
         
       
      
    def tokenize(self):
        result = []
        
        while self.currentChar is not None:
            if re.match(r'\s', self.currentChar):
                self.getNextChar()
            elif re.match(r'[a-z]', self.currentChar):
                result.append(self.makeCharacter())
            elif re.match(r'\d', self.currentChar):
                response, error = self.makeDigit()
                if(response is not None):
                    result.append(response)
                else:
                    return None, error;
            elif self.currentChar in ['{', '}', '(', ')']:
                result.append(self.bracket(self.currentChar))
                self.getNextChar()
            elif self.currentChar in ['+', '-', '*', '/', '^']:
                result.append(self.operationSign(self.currentChar))
                self.getNextChar()
            elif self.currentChar == '=':
                result.append(Token(constant.EQ, self.currentChar))
                self.getNextChar()
            elif self.currentChar == ',':
                result.append(Token(constant.COMMA, ','))
                self.getNextChar()
            elif re.match(r'\W', self.currentChar):
                return None, ErrorTask('Illegal Character', self.currentChar )
             
               
        return result, ErrorTask('','')
    
    
    def makeCharacter(self):
        n = ''
        while self.currentChar is not None and re.match(r'[a-z]', self.currentChar):
             n = n+self.currentChar
             self.getNextChar()
             
        if n in res_word:
            return Token('Reserved', n)
        else:
            return Token('Var', n)

    def makeDigit(self):
        n = ''; dotCounter = 1
        while self.currentChar is not None and re.match(r'\d', self.currentChar) or  self.currentChar == '.':
             n = n+self.currentChar
             if dotCounter < 2 and self.currentChar == '.':
                 dotCounter += 1 
             elif dotCounter >= 2 and self.currentChar == '.':
                return None, ErrorTask('Multiple Dot',n)
             self.getNextChar()
             
        if   '.' in n:
            return Token(constant.FLOAT, n), None
        else:
            return Token(constant.INT, n), None
    
    def operationSign(self, sign):
        if sign == '+':
            return Token(constant.PLUS, sign)
        elif sign == '-':
            return Token(constant.MINUS, sign)
        elif sign == '*':
            return Token(constant.MUL, sign)
        elif sign == '/':
            return Token(constant.DIV, sign)
        else:
            return Token(constant.CARET, sign)
        
    def bracket(self, symbol):
        if symbol == '{':
            return Token(constant.LCURY, symbol)
        elif symbol == '}':
            return Token(constant.RCURY, symbol)
        elif symbol == '(':
            return Token(constant.LPAREN, symbol)
        else:
            return Token(constant.RPAREN, symbol)
        
                
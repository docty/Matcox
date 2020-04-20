# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:59:01 2020

@author: Lenovo G50
"""

 
class ErrorTask:
    
    def __init__(self, errorMessage, errorValue=''):
        self.errorMessage = errorMessage
        self.errorValue = errorValue
        
        
    def __repr__(self):
        return self.errorMessage+': '+ self.errorValue
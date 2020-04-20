



class Token:
    
    
    
    def __init__(self, _type, value):
        self._type = _type
        self.value = value
        
        
    def __repr__(self):
       return '{'+self._type+':'+self.value+ '}'
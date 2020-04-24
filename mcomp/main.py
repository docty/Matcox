
try: 
    from lexer import Lexer
    from passer import Passer
    from solve import Solve
    from base import Base
    from evaluate import Evaluate
except ImportError:
    from .lexer import Lexer
    from .passer import Passer
    from .solve import Solve
    from .base import Base
    from .evaluate import Evaluate





def run():
     
    try:
        file = open('./board.mc', 'r')
        text = file.read()
    except FileNotFoundError :
        file = open('../board.mc', 'r')
        text = file.read()
    file.close()

    lex = Lexer(text)
    token, error = lex.tokenize()
    
    if (token is  None):
        return error
    else:
        passer = Passer(token)
        rule, error = passer.grammar()
        
        if rule is None:
            return error
        else:
            
            if(token[0].value == 'solve') :
                sol = Solve(rule[2:])
                return sol.useCaseTest()
            elif (token[0].value == 'base') :
                bases = Base(rule[2:])
                return bases.results()
            elif (token[0].value == 'evaluate') :
                eva = Evaluate(rule[2:-1])
                return eva.useCaseTest()
    



if __name__ == '__main__':
    print(run())


def callRunner():
    return run()


 
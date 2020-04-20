try: 
    from lexer import Lexer
    from passer import Passer
    from evaluate import Evaluate
    from base import Base
except ImportError:
    from .lexer import Lexer
    from .passer import Passer
    from .evaluate import Evaluate
    from .base import Base





def run():
     
    file = open('./board.mc', 'r')
    text = file.read()
    file.close()

    lex = Lexer(text)
    token, error = lex.tokenize()
    
    if (token is  None):
        print(error)
    else:
        passer = Passer(token)
        rule, error = passer.grammar()

        if rule is None:
            print(error)
        else:
            if(token[0].value == 'solve') :
                eva = Evaluate(rule[2:])
                return eva.useCaseTest()
                # print(eva.expression())
            elif (token[0].value == 'base') :
                bases = Base(rule[2:])
                return bases.results()
    



if __name__ == '__main__':
    print(run())


def callRunner():
    return run()


 
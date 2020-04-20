# Grammar Rule Defintion




integer = [0-9]
term = integer
expression = term,(plus|minus),term
bracket = { \ }
reserved = solve

grammar = reserved, bracket, expression, bracket
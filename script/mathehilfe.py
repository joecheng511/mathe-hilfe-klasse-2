import sys
from random import randrange
 
OPERATOR_TUPLE = ('+', '-', '*', '/')

score = 0

while True:
    operator = OPERATOR_TUPLE[randrange(0, len(OPERATOR_TUPLE))]
    A = 0
    B = 0   
    if operator == '+':
        A = randrange(100)
        B = randrange(100)
    elif operator == '-':
        A = randrange(100)
        B = randrange(A)
    elif operator == '*':
        A = randrange(100)
        B = randrange(10)
    elif operator == '/':
        answer = randrange(10)
        B = randrange(1, 100)
        A = answer * B
    question_string = '{} {} {} '.format(A, operator, B)
    answer = int(eval(question_string))
    print(question_string + ' = ?')
    
    for line in sys.stdin:
        if str(answer) == str(line.rstrip()):
            break
        print('Falsch!')
    score += 100
    print("Richtig! Punkte: {} \n\n".format(score))


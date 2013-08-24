import operator
ops = { 
    '+': operator.add, 
    '-': operator.sub, 
    '*': operator.mul,
    '/': operator.truediv
    }


firstNumber = int(raw_input('Enter the first number: '))
userOperator = raw_input('Choose an operator (+ - * /): ')
secondNumber = int(raw_input('Enter a second number: '))

print ops[userOperator](firstNumber, secondNumber)

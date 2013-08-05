import helpers

def fibonacci(number):
    a, b = 0, 1
    while b < number:
        print b,
        a, b = b, a + b
    print number
    

userMessage = 'Do fibonacci for a specific interval. Enter a number:'
userInput = int(helpers.getUserInput(userMessage))
outcome = fibonacci(userInput)

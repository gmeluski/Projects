import helpers

def generatePrimeFromPoint(startPoint):
    primeTest = helpers.isPrime(startPoint)
    while (not primeTest):
        startPoint += 1
        if (startPoint % 2 != 0):
            primeTest = helpers.isPrime(startPoint)
    return startPoint

def primeMessage(numberForMessage):
    print 'Last prime is',
    print numberForMessage,
    print '. Do you want to find the next prime? (Y)'
    userInput = raw_input() 
    return True if (userInput == 'Y' or userInput == 'y') else False

startPoint = 2
userResult = primeMessage(startPoint)
while (userResult):
    startPoint += 1
    startPoint = generatePrimeFromPoint(startPoint)
    userResult = primeMessage(startPoint)

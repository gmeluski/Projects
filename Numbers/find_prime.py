import helpers

# generate primeFromPoint(startPoint)
#    primeTest = isPrime(startPoint)
#    if primeTest
#       return startPoint
#   else
#       while (!primeTest)
#           startPoint equals startPoint + 1
#           if startPoint mod 2 does not equal 0
#               primeTest = isPrime(startPoint)
#        

def generatePrimeFromPoint(startPoint):
    primeTest = helpers.isPrime(startPoint)
    while (not primeTest):
        startPoint = startPoint + 1
        if (startPoint % 2 != 0):
            primeTest = isPrime(startPoint)   
    return startPoint

def primeMessage(numberForMessage):
    print 'Last prime is',
    print numberForMessage,
    print '. Do you want to find the next prime? (Y)'
    userInput = raw_input() 
    return True if (userInput == 'Y' or userInput == 'y') else False

startPoint = 2
userResult = primeMessage(startPoint)
if (userResult):
    generatePrimeFromPoint(startPoint)

# print lastPrime, then a prompt to continue
# if continue
#   generate a prime number based on the last number
# else 
#   print goodbye!

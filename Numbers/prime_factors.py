import helpers

def isPrime(numberToCheck):
    # for every number between the given number and 2, make sure it does NOT divide evenly
    for divisor in range(2, numberToCheck):
        if (numberToCheck % divisor == 0):
            return False
    return True    

def findPrimeFactors(numberToCheck):
    if (isPrime(numberToCheck)):
        print numberToCheck
        return True
    else:
        print 'range'
        for divisor in range(2, numberToCheck):
            if (numberToCheck % divisor == 0):
                # find the other number
                print divisor
                print isPrime(divisor)
                foundFactor = numberToCheck / divisor
                print foundFactor
                print isPrime(foundFactor)
                return

# if the original number is prime, just return the original number
# otherwise start a counter / range at 2
# if this number divides evenly
#   log the original counter
#   find the other number.
#   if that number is prime
#       log that number
# while the modulo is 0
#   get the other number


userMessage = 'Enter a number to find all prime factors:'
originalNumber = int(helpers.getUserInput(userMessage))
print findPrimeFactors(originalNumber)

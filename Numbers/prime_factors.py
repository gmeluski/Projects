import helpers

def isPrime(numberToCheck):
    # for every number between the given number and 2, make sure it does NOT divide evenly
    for divisor in range(2, numberToCheck):
        if (numberToCheck % divisor == 0):
            return False
    return True    

def findPrimeFactors(numberToCheck):
    if (isPrime(numberToCheck)):
        print numberToCheck,
        return True
    else:
        for divisor in range(2, numberToCheck):
            if (numberToCheck % divisor == 0):
                # find the other number
                print divisor,
                if (isPrime(divisor)):
                    foundFactor = numberToCheck / divisor
                    findPrimeFactors(foundFactor) 
                return

userMessage = 'Enter a number to find all prime factors:'
originalNumber = int(helpers.getUserInput(userMessage))
findPrimeFactors(originalNumber)

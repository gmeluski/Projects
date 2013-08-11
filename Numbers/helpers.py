def representsInteger(numberToTest):
    try:
        int(numberToTest)
        return True
    except ValueError:
        return False

def getUserInput(userMessage):
    print userMessage
    userEntry = raw_input()
    return userEntry


def isPrime(numberToCheck):
    # for every number between the given number and 2, make sure it does NOT divide evenly
    for divisor in range(2, numberToCheck):
        if (numberToCheck % divisor == 0):
            return False
    return True    

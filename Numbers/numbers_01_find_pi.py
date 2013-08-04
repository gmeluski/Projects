import helpers
from sympy.mpmath import mp

def representsInteger(numberToTest):
    try:
        int(numberToTest)
        return True
    except ValueError:
        return False

def getUserInput():
    print 'Find pi to a certain place. Enter a number:'
    userEntry = raw_input()
    return userEntry

userInput = getUserInput()
mp.dps = int(userInput)
print(mp.pi)

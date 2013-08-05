import helpers
from sympy.mpmath import mp

userMessage = 'Find pi to the nth place. Enter a number:' 
userInput = helpers.getUserInput(userMessage)
mp.dps = int(userInput)
print(mp.pi)

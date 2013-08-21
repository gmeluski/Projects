import helpers

originalDecimal = int(helpers.getUserInput('Enter a number to convert'))
newBinary = bin(originalDecimal)
print newBinary
print int(newBinary, 2)

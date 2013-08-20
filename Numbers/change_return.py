#The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

import operator
import math

def changeDivision(amountToDivide, coinage): 
    floatDivision = amountToDivide / coinage 
     
    if (floatDivision < 1 and floatDivision > 0):
        numberOfCoins = 1
        newChange = round(amountToDivide, 2) - round(coinage, 2)
    else:
        numberOfCoins = int(floatDivision); 
        newChange = amountToDivide % coinage
    
    return [numberOfCoins, newChange]

def findChange(change) :
    changeResults = {
        'quarters' : 0,
        'dimes' : 0,
        'nickels' : 0,
        'pennies' : 0
    }
    
    changeValues = {
        'quarters' : 0.25,
        'dimes' : 0.10,
        'nickels' : 0.05,
        'pennies' : 0.01,
    }   

    sortedChangeValues = sorted(changeValues.items(), key=operator.itemgetter(1))
    sortedChangeValues.reverse()

    for key,value in sortedChangeValues:
        if (change > 0):
            returnData = changeDivision(change, value)
            changeResults[key] = returnData[0]
            change = returnData[1]

    print changeResults

cost = float(raw_input('Enter the cost: '))
paid = float(raw_input('Enter the amount given: '))

change = paid - cost
findChange(change)

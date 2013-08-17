#The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

import operator

def changeDivision(amountToDivide, coinage): 
    numberOfCoins = int(amountToDivide / coinage)
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
        print key 

    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01
    
    if (change > quarter) :
        returnData = changeDivision(change, quarter)
        changeResults['quarters'] = returnData[0]
        print returnData[0]
        print returnData[1]



cost = float(raw_input('Enter the cost: '))
paid = float(raw_input('Enter the amount given: '))

change = paid - cost
findChange(change)

#The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

def ChangeDivision(amountToDivide, coinage) {

}

def findChange(change) {
    changeResults = {
        'quarters' : 0,
        'dimes' : 0,
        'nickels' : 0,
        'pennies' : 0
    }
    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01
    
    if (change > quarter) {
        numberOfQuarters = int(change / quarter)
        newChange = change % quarter
    } elif (change > dime) {

    }

}



cost = float(raw_input('Enter the cost: '))
paid = float(raw_input('Enter the amount given: '))

change = cost - paid 



print numberOfQuarters
print newChange

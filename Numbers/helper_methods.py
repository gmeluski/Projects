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

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

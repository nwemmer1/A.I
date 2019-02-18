# Utilized for terminating program with sys.exit()
import sys


def executeProgram():
    # Infinite loop until quit is selected
    while(True):
        displayMenu()
        executeSelectedItem(collectAndValidateMain())


def displayMenu():
    print("Available options:")
    print("1. Learn a decision tree from training data.")
    print("2. Save the tree learned in menu item 1.")
    print("3. Applying the decision tree to new cases.")
    print("4. Load a tree model saved previously and apply the model to new cases interactively as in menu item 3")
    print("5. Quit")


def collectAndValidateMain():
    userInput = int(input("Enter your choice:"))
    isInvalid = True
    while (isInvalid):
        if (userInput > 5 or userInput < 1):
            userInput = int(input(
                "Invalid input. Please enter a number between 1 and 5:"))
        else:
            isInvalid = False
            return userInput


def collectandValidateSub():
    userInput = int(input("Enter your choice:"))
    isInvalid = True
    while (isInvalid):
        if (userInput > 2 or userInput < 1):
            userInput = int(input(
                "Invalid input. Please enter a number between 1 and 2:"))
        else:
            isInvalid = False
            return userInput


def executeSelectedItem(userInput):
    if (userInput == 1):
        learnTree()
    elif (userInput == 2):
        saveTree()
    # Option 3 requires additional menu and input validation
    elif (userInput == 3):
        print("1. Enter a new case interactively.")
        print("2. Quit.")
        subMenuInput = collectandValidateSub()
        if (subMenuInput == 1):
            interactiveNewCase()
        else:
            return
    elif (userInput == 4):
        loadPreviousTreeForNewCases()
    else:
        terminateProgram()


def learnTree():
    return


def saveTree():
    return


def interactiveNewCase():
    return


def loadPreviousTreeForNewCases():
    return


def terminateProgram():
    sys.exit("Program terminated.")

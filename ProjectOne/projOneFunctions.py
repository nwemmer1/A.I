# Andrew Welch  <abw28@zips.uakron.edu>  2700340
# A.I Project 1

import sys
from sklearn import datasets
from sklearn import tree


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
    print("Enter your choice: ")
    userInput = int(input())
    isInvalid = True
    while (isInvalid):
        if (userInput > 5 or userInput < 1):
            print("Invalid input. Please enter a number between 1 and 5: ")
            userInput = int(input())
        else:
            isInvalid = False
            return userInput


def collectandValidateSub():
    userInput = int(input("Enter your choice (1 or 2): "))
    isInvalid = True
    while (isInvalid):
        if (userInput > 2 or userInput < 1):
            print("Invalid input. Please enter a number between 1 and 2: ")
            userInput = int(input())
        else:
            isInvalid = False
            return userInput


def collectTrainingExampleFiles():
    print("The following datasets are available for creating a decision tree: ")
    print("1. iris  2. wine")
    fileChoice = collectandValidateSub()
    if (fileChoice == 1):
        from sklearn.datasets import load_iris
        iris = load_iris()
        return iris
    else:
        from sklearn.datasets import load_wine
        wine = load_wine()
        return wine


def executeSelectedItem(userInput):
    if (userInput == 1):
        collectTrainingExampleFiles()
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

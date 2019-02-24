# Andrew Welch  <abw28@zips.uakron.edu>  2700340
# A.I Project 1

import sys
from sklearn import tree
from sklearn.tree import _tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import pickle
import pandas as pd


# Flag for saving decision trees
treeGenerated = False
# Global decisionTree and dataset (band-aid fix)
decisionTree = tree.DecisionTreeClassifier()
dataset = load_iris()


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


def selectDataset():
    print("The iris and wine data sets are available for testing or you may input your own .csv data set:")
    print("1. iris  2. wine  3. enter a file name")
    fileChoice = int(input())
    if (fileChoice == 1):
        return True
    elif (fileChoice == 2):
        global dataset
        dataset = load_wine()
        return True
    else:
        return False


def learnTree():
    global dataset
    global decisionTree
    decisionTree = decisionTree.fit(dataset.data, dataset.target)
    global treeGenerated
    treeGenerated = True


def displayTree():
    import graphviz
    plotData = tree.export_graphviz(decisionTree, out_file=None, feature_names=dataset.feature_names, class_names=dataset.target_names,
                                    filled=True, rounded=True,
                                    special_characters=True)
    treeGraph = graphviz.Source(plotData)
    pdfName = input("Enter a valid name for the pdf (do not include .pdf) ")
    treeGraph.render(pdfName)
    print("A pdf has been generated displaying the decision tree generated!")
    pause = input("PRESS ENTER TO CONTINUE")


def saveTree():
    fileName = input(
        "Enter a name to save the decision tree as (include .sav type extension): ")
    saveFile = open(fileName, 'wb')
    pickle.dump(decisionTree, saveFile)
    print("The decision tree has been saved!")
    pause = input("PRESS ENTER TO CONTINUE")


def formatInputDatasetAndMakeTree():
    import pandas as pd
    global dataset
    dataName = input(
        "Enter the file name for data set you wish to use (include .csv): ")
    dataset = pd.read_csv(dataName, delimiter=',')
    X = dataset.drop('Class', axis=1)
    y = dataset['Class']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    decisionTree.fit(X_train, y_train)
    global treeGenerated
    treeGenerated = True
    print("Tree generated! Here are the specifications of the tree: ")
    print(decisionTree)
    pause = input("PRESS ENTER TO CONTINUE")


def terminateProgram():
    sys.exit("Program terminated.")


def executeSelectedItem(userInput):
    # Menu item 1
    if (userInput == 1):
        if (selectDataset()):
            learnTree()
            displayTree()
        else:
            formatInputDatasetAndMakeTree()
    # Menu item 2
    elif (userInput == 2):
        if (treeGenerated):
            saveTree()
        else:
            print("ERROR: You have not created a decision tree yet!")
            return
    # Menu item 3
    elif (userInput == 3):
        if (treeGenerated):
            print("1. Enter a new case interactively.")
            print("2. Quit.")
            subMenuInput = collectandValidateSub()
            if (subMenuInput == 1):
                traverseTreeInteractively()
            else:
                return
        else:
            print("ERROR: You have not created a decision tree yet!")
            return

    # Menu item 4
    elif (userInput == 4):
        loadPreviousTreeForNewCases()
    # Menu item 5
    else:
        terminateProgram()


def loadPreviousTreeForNewCases():
    global decisionTree
    fileName = input(
        "Enter the file name of the decision tree you wish to load (include type extension .sav): ")
    decisionTree = pickle.load(open(fileName, 'rb'))
    global dataset
    if (dataset == load_iris()):
        dataset = load_wine()
    else:
        dataset = load_iris()
    traverseTreeInteractively()
    return


def traverseTreeInteractively():
    global dataset
    global decisionTree
    tree_ = decisionTree.tree_
    feature_names = dataset.feature_names
    target_names = dataset.target_names
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]

    def recurse(node, depth, count):
        if (tree_.feature[node] != _tree.TREE_UNDEFINED):
            variableName = feature_name[node]
            nodeThreshold = tree_.threshold[node]
            print("Input a value for ", variableName, ": ")
            print("The threshold value at this node is: ", nodeThreshold)
            inputValue = int(input())
            if (inputValue <= nodeThreshold):
                recurse(tree_.children_left[node], depth + 1, count + 1)
            else:
                recurse(tree_.children_right[node], depth + 1, count + 1)
        else:
            print("A leaf has been reached!")
            if (count == 1):
                print("Your inputs resulted in the ",
                      target_names[0], " class")
            elif (count < 4):
                print("Your inputs resulted in the ",
                      target_names[2], " class")
            else:
                print("Your inputs resulted in the ",
                      target_names[1], " class")
            pause = input("PRESS ENTER TO CONTINUE")

    recurse(0, 1, 0)
    return

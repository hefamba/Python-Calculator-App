from add import *
from subtract import *
from getUserInput import *
from multiply import *
from divide import *
from square import *


def displayMainMenu():
    print("*********** Main Menu ***********")
    print("Enter 1 for Addition")
    print("Enter 2 for Subtraction")
    print("Enter 3 for Multiplication")
    print("Enter 4 for Division")
    print("Enter 5 to square a number")
    print("Enter 0 to exit")
    print("*********************************")



def main():
    done = 0

    while done == 0:
        displayMainMenu()
        print("Please enter a menu choice")
        menuChoice = getUserInput()
        results = 0

        if menuChoice == 1:
            results = add()
        elif menuChoice == 2:
            results = subtract()
        elif menuChoice == 3:
            results = multiply()
        elif menuChoice == 4:
            results = divide()
        elif menuChoice == 5:
            results = square()
        elif menuChoice == 0:
            done = -1
            print("Thank your for using my app. Bye!")
            break
        else:
            print("Please choose a valid choice")
            continue

        print("Results : " + str(results))


if __name__ == '__main__':
    main()

def help_screen():
    """
    Displays information about how the program works.
    Accepts no parameters.
    Returns nothing.
    """
    print("Add: adds to numbers")
    print("Subtract: Subtracts two numbers")
    print("Print: Displays the result of the latest operation")
    print("Help: Displays the help screen")

def menu():
    """
    Displays a menu
    Accepts no parameters
    Returns the string entered by the user.
    """

    return input("=== A)dd S)ubtract P)rint H)elp Q)uit ===")

def main():
    """ Runs a command loop that allows users to perform simple arithmetic. """
    result = 0.0
    done = False
    while not done:
        choice = menu()

        if choice == "A" or choice == "a":
            arg1 = float(input("Enter arg 1: "))
            arg2 = float(input("Enter arg 2: "))
            result = arg1 + arg2
            print(result)
        elif choice == "S" or choice == "s":
            arg1 = float(input("Enter arg 1: "))
            arg2 = float(input("Enter arg 2: "))
            result = arg1 - arg2
            print(result)
        elif choice == "P" or choice == "p":
            print(result)
        elif choice == "H" or choice == "h":
            help_screen()
        elif choice == "Q" or choice == "q":
            done = True

main()

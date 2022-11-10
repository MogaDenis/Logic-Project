# TODO - construct a menu-driven application...

import implementations


def print_main_menu():
    """
        This function prints to the console the options inside the main menu from which the user can choose.
    """

    print("\nWhat would you like to do?\n")
    print("1 - Perform calculations with positive integers.")
    print("2 - Convert a number from a base to another using a certain method.")
    print("0 - Close the application.\n")


def print_sub_menu1():
    """
        This function prints to the console the options inside the sub menu corresponding to the 
        calculations part from which the user can choose.
    """

    print("\n\tWhat would you like to do?\n")
    print("\t1 - Add two numbers in a base.")
    print("\t2 - Subtract two numbers in a base.")
    print("\t3 - Multiply a number by a digit in a base.")
    print("\t4 - Divide a number by a digit in a base.")
    print("\t0 - Return to the main menu.\n")    


def print_sub_menu2():
    """
        This function prints to the console the options inside the sub menu corresponding to the 
        calculations part from which the user can choose.
    """

    print("\n\tWhat would you like to do?\n")
    print("\t1 - Convert a number between to bases using Successive Division Method.")
    print("\t2 - Convert a number between to bases using Substitution Method.")
    print("\t3 - Convert a number between to bases using Rapid Conversions Method.")
    print("\t0 - Return to the main menu.\n") 


def read_base_and_two_numbers(restriction=False):

    base = input("Please enter the base: ")

    while not base.isnumeric() or base == '1':
        print("Invalid input! The base must be a positive integer greater than 1!")
        base = input("Please enter the base: ")

    base = int(base)

    number1 = input("Please enter the first number: ").upper()

    while not implementations.check_if_valid_representation(number1, base):
        print(f"Invalid input! The number given can't be written in base {base}!")
        number1 = input("Please enter the first number: ").upper()

    message = "Please enter the second number: "

    if restriction:
        message = "Please enter a digit: "

    number2 = input(message).upper()

    while not implementations.check_if_valid_representation(number2, base):
        print(f"Invalid input! The number given can't be written in base {base}!")
        number2 = input(message).upper()

    if restriction:
        while len(number2) != 1:
            print("Invalid input! The second number must be a single digit!")
            number2 = input(message).upper()

    return base, number1, number2


def main():
    """
        This is the main function which starts the execution of the menu-driven application.
    """

    main_menu_option = '-1'

    while main_menu_option != '0':
        
        print_main_menu()

        main_menu_option = input("Your choice is: ")

        if main_menu_option == '1':
            # Perform calculations.

            while True:
                print_sub_menu1()

                sub_menu1_option = input("Your choice is: ")

                if sub_menu1_option == '1':
                    # Perform addition of two numbers. 
                    
                    base, number1, number2 = read_base_and_two_numbers()

                    result = implementations.add_numbers_in_a_base(number1, number2, base)

                    print(f"\n\t{number1}({base}) + {number2}({base}) = {result}({base})")

                elif sub_menu1_option == '2':
                    # Perform subtraction of two numbers. 
                    
                    base, number1, number2 = read_base_and_two_numbers()

                    result = implementations.subtract_numbers_in_a_base(number1, number2, base)

                    print(f"\n\t{number1}({base}) - {number2}({base}) = {result}({base})")

                elif sub_menu1_option == '3':
                    # Perform multiplication of a number by a digit.     
                    
                    base, number1, number2 = read_base_and_two_numbers(restriction=True)

                    result = implementations.multiplication_with_one_digit(number1, number2, base)

                    print(f"\n\t{number1}({base}) * {number2}({base}) = {result}({base})")

                elif sub_menu1_option == '4':
                    # Perform division of a number by a digit. 
                    
                    base, number1, number2 = read_base_and_two_numbers(restriction=True)

                    quotient, remainder = implementations.division_by_one_digit(number1, number2, base)

                    remainder_string = ""

                    if remainder != '0':
                        remainder_string = f"remainder {remainder}({base})"

                    print(f"\n\t{number1}({base}) ÷ {number2}({base}) = {quotient}({base}) {remainder_string}")

                elif sub_menu1_option == '0':
                    break

                else:
                    print("\nInvalid input!")
            

        elif main_menu_option == '2':
            # Convert numbers

            while True:

                sub_menu2_option = input("Your choice is: ")

                if sub_menu2_option == '1':
                    # Convert by successive divisions method
                    # Allow it only if final base < initial base
                    pass

                elif sub_menu2_option == '2':
                    # Convert by substitution method
                    # Allow it only if final base > initial base
                    pass

                elif sub_menu2_option == '3':
                    # Convert by rapid conversions. 
                    # Allow it only if initial base and final base are in [2, 4, 8, 16]
                    pass

                elif sub_menu2_option == '0':
                    break

                else:
                    print("\nInvalid input!")
        
        elif main_menu_option == '0':
            break

        else:
            print("\nInvalid input!")


main()
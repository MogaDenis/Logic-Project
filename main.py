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
    print("\t1 - Convert a number between to bases using Successive Division Method. (initial base > destination base)")
    print("\t2 - Convert a number between to bases using Substitution Method. (initial base < destination base)")
    print("\t3 - Convert a number between to bases using Rapid Conversions Method. (initial and destination base must be 2, 4, 8 or 16)")
    print("\t4 - Convert a number between to bases using base 10 as an intermediate base. (any bases between 2 and 16)")
    print("\t0 - Return to the main menu.\n") 


def read_base_and_two_numbers(restriction=False):

    base = input("Please enter the base: ")

    while not base.isnumeric() or base == '1' or int(base) > 16:
        print("Invalid input! The base must be a positive integer greater than 1 and less than or equal to 16!")
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


def read_number_and_two_bases():

    initial_base = input("Please enter the base of the number you want to convert: ")

    while not initial_base.isnumeric() or initial_base == '1' or int(initial_base) > 16:
        print("\nInvalid input! The base must be a positive integer greater than 1 and less than or equal to 16!\n")
        initial_base = input("Please enter the base of the number you want to convert: ")

    initial_base = int(initial_base)

    number = input("Please enter the number to convert: ").upper()

    while not implementations.check_if_valid_representation(number, initial_base):
        print(f"Invalid input! The number given can't be written in base {initial_base}!")
        number = input("Please enter the first number: ").upper()

    destination_base = input("Please enter the base in which you want to convert the given number: ")

    while not destination_base.isnumeric() or destination_base == '1' or int(destination_base) > 16:
        print("\nInvalid input! The base must be a positive integer greater than 1 and less than or equal to 16!\n")
        destination_base = input("Please enter the base in which you want to convert the given number: ")

    destination_base = int(destination_base)

    return number, initial_base, destination_base


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
                print_sub_menu2()

                sub_menu2_option = input("Your choice is: ")

                if sub_menu2_option == '1':
                    # Convert by successive divisions method
                    # Allow it only if final base <= initial base
                    
                    number, initial_base, destination_base = read_number_and_two_bases()

                    if initial_base >= destination_base:
                        converted_number = implementations.successive_divisions_conversion_method(number, initial_base, destination_base)

                        print(f"\n{number}({initial_base}) = {converted_number}({destination_base})")

                    else:
                        print("\nCan't perform the conversion. "
                        "Successive divisions method is not recommended if the destination is greater than the initial base.")

                elif sub_menu2_option == '2':
                    # Convert by substitution method
                    # Allow it only if final base > initial base
                    
                    number, initial_base, destination_base = read_number_and_two_bases()

                    if initial_base <= destination_base:
                        converted_number = implementations.substitution_conversion_method(number, initial_base, destination_base)

                        print(f"\n{number}({initial_base}) = {converted_number}({destination_base})")

                    else:
                        print("\nCan't perform the conversion. "
                        "Substitution method is not recommended if the destination is less than the initial base.")

                elif sub_menu2_option == '3':
                    # Convert by rapid conversions. 
                    # Allow it only if initial base and final base are in [2, 4, 8, 16]
                    
                    number, initial_base, destination_base = read_number_and_two_bases()

                    if initial_base in [2, 4, 8, 16] and destination_base in [2, 4, 8, 16]:
                        converted_number = implementations.rapid_conversions(number, initial_base, destination_base)

                        print(f"\n{number}({initial_base}) = {converted_number}({destination_base})")

                    else:
                        print("\nCan't perform the conversion. "
                        "Rapid conversions method can be performed only if both bases are either 2, 4, 8 or 16.")

                elif sub_menu2_option == '4':
                    # Convert using 10 as an intermediate base.  

                    number, initial_base, destination_base = read_number_and_two_bases()

                    decimal_number = implementations.substitution_method_conversion_to_decimal(number, initial_base)

                    converted_number = implementations.successive_divisions_conversion_from_decimal(decimal_number, destination_base)

                    print(f"\n{number}({initial_base}) = {decimal_number}(10) = {converted_number}({destination_base})")

                elif sub_menu2_option == '0':
                    break

                else:
                    print("\nInvalid input!")
        
        elif main_menu_option == '0':
            break

        else:
            print("\nInvalid input!")


main()
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

    print("\nWhat would you like to do?\n")
    print("1 - Add two numbers in a base.")
    print("2 - Subtract two numbers in a base.")
    print("3 - Multiply a number by a digit in a base.")
    print("4 - Divide a number by a digit in a base.")
    print("0 - Return to the main menu.\n")    


def take_input_and_check_if_valid_option(list_of_options):
    """
        This function requires the user to input and option and checks if it is a valid one.

        The user is required to enter inputs until he enters a valid one.
    Args:
        list_of_options (List of strings): This list contains the valid options the user can choose from.

    Returns:
        String: The valid option chose by the user
    """
    
    user_option = input("Your choice is: ")

    while user_option not in list_of_options:
        print("\nInvalid input!\n")

        user_option = input("Your choice is: ")

    return user_option


def main():
    """
        This is the main function which starts the execution of the menu-driven application.
    """

    main_menu_option = '-1'

    while main_menu_option != '0':
        
        print_main_menu()

        main_menu_option = take_input_and_check_if_valid_option(['0', '1', '2'])

        if main_menu_option == '1':
            # Perform calculations.
            
            sub_menu1_option = '-1'

            while sub_menu1_option != '0':
                print_sub_menu1()

                sub_menu1_option = take_input_and_check_if_valid_option(['0', '1', '2', '3', '4'])

                if sub_menu1_option == '1':
                    # Perform addition of two numbers. 
                    pass

                elif sub_menu1_option == '2':
                    # Perform subtraction of two numbers. 
                    pass

                elif sub_menu1_option == '3':
                    # Perform multiplication of a number by a digit.     
                    pass 

                elif sub_menu1_option == '4':
                    # Perform division of a number by a digit. 
                    pass
            

        elif main_menu_option == '2':
            # Convert numbers
            pass


main()
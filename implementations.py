import auxiliary

#################################################
#   Made by Moga Denis-Andrei from Group 915.   # 
#################################################


def check_if_valid_representation(number, base):
    """
        This function checks if a given number is correctly represented in the given base. (Checks if there are digits that
    are not available in the given base)

    :return: True - if the representation is valid and False, otherwise
    """

    for digit in number:
        if digit != '-' and auxiliary.characters.index(digit) >= base:
            return False

    return True


def add_numbers_in_a_base(number1, number2, base):
    """
        This function adds two numbers in a given base from 2 to 16.

    :param number1: String
    :param number2: String
    :param base: Integer representing the base in which are the numbers given.
    :return: String representing the sum of the two given numbers represented in the given base.
    """

    # This string will contain the result of the addition.
    result = ""

    i = len(number1) - 1
    j = len(number2) - 1

    # This is the carry digit.
    carry = 0

    # The addition will take place similarly to a merge.
    # We add the corresponding digits starting from the right and going to the left.
    while i >= 0 and j >= 0:
        # Extract the decimal value of the digits to be added.
        digit1 = auxiliary.characters.index(number1[i])
        digit2 = auxiliary.characters.index(number2[j])

        # Calculate the sum of digits and also add the carry.
        sum_of_digits = digit1 + digit2 + carry

        # The new digit in decimal is the remainder of the sum divided by the base in which we do the addition.
        new_digit = sum_of_digits % base

        # Add the digit in the corresponding base in the result.
        result = auxiliary.characters[new_digit] + result

        # The transport digit for the next operation is the quotient of the sum divided by the base.
        carry = sum_of_digits // base

        i -= 1
        j -= 1

    # This block of code will execute only if the first number has more digits than the second one.
    # We basically add the digits at the front of the result, keeping track of the transport digit.
    while i >= 0:
        digit = auxiliary.characters.index(number1[i])

        sum_of_digits = digit + carry

        new_digit = sum_of_digits % base

        result = auxiliary.characters[new_digit] + result

        carry = sum_of_digits // base

        i -= 1

    # This block of code will execute only if the second number has more digits than the first one.
    # We basically add the digits at the front of the result, keeping track of the transport digit.
    while j >= 0:
        digit = auxiliary.characters.index(number2[j])

        sum_of_digits = digit + carry

        new_digit = sum_of_digits % base

        result = auxiliary.characters[new_digit] + result

        carry = sum_of_digits // base

        j -= 1

    # If we have a transport digit outside the max(len(number1), len(number2)), then we add it at the front.
    if carry != 0:
        result = str(carry) + result

    # Return the sum of the two numbers as a string.
    return result


def compare(number1, number2, base):
    """
        This is a helper function which compares two numbers given in a certain base.

    :param number1: String
    :param number2: String
    :param base: Integer representing the base in which are the numbers given.
    :return: True - if number1 < number2
             False - otherwise
    """

    # If the length of the first number is less than the one of the second's number, then it means number1 < number2
    if len(number1) < len(number2):
        return True

    # If the length of the first number is greater than the one of the second's number, then it means number1 > number2
    elif len(number1) > len(number2):
        return False

    # If the lengths of both numbers are equal we have to check their digits from left to right.
    else:
        i = 0
        j = 0

        while i < len(number1) and j < len(number2):
            digit1 = auxiliary.characters.index(number1[i])
            digit2 = auxiliary.characters.index(number2[j])

            # If the corresponding digit of the first value is less than the one corresponding to the second one, then
            # it means that number1 < number2
            if digit1 < digit2:
                return True

            i += 1
            j += 1

    # If we got here it means that number1 >= number2
    return False


def subtract_numbers_in_a_base(number1, number2, base):
    """
        This function subtracts to numbers in a base from 2 to 16.

    :param number1: String
    :param number2: String
    :param base: Integer representing the base in which the numbers are represented.
    :return: String representing the difference of the two given numbers represented in the given base.
    """

    # This string will store the result of the subtraction.
    result = ""

    # If this boolean variable is true it means that number1 < number2, so the result of the subtraction will be
    # negative.
    swapped = False

    # Check if the result will be negative or positive.
    # Swap the elements, so we get the result in absolute value, and we add after the operations '-' in the front of the
    # result.
    if compare(number1, number2, base):
        aux = number1
        number1 = number2
        number2 = aux
        swapped = True

    i = len(number1) - 1
    j = len(number2) - 1

    # This will be the borrow digit.
    borrow = 0

    # The subtraction will take place similarly to a merge.
    # We subtract the corresponding digits starting from the right and going to the left.
    while i >= 0 and j >= 0:
        # Extract the decimal values of the digits to be subtracted
        digit1 = auxiliary.characters.index(number1[i])
        digit2 = auxiliary.characters.index(number2[j])

        # Subtract the two digits and also the borrow.
        diff_of_digits = digit1 - digit2 - borrow

        # If the difference is negative, add the base to the obtained value and store it as a new digit and set the
        # borrow to 1.
        if diff_of_digits < 0:
            new_digit = diff_of_digits + base
            borrow = 1

        # Otherwise, set the borrow back to 0 and store the obtained value as a new digit.
        else:
            borrow = 0
            new_digit = diff_of_digits

        # Add to the result the value of the new digit in the required base.
        result = auxiliary.characters[new_digit] + result

        i -= 1
        j -= 1

    # This block of code will execute only if the first number has more digits than the second one.
    # We know for sure the first number has a number of digits greater or equal to the second one because we checked
    # at the beginning if the first one is less than the second one, and we swapped them if that was the case.
    # We basically add the digits at the front of the result, keeping track of the transport digit.
    while i >= 0:
        digit = auxiliary.characters.index(number1[i])

        diff_of_digits = digit - borrow

        if diff_of_digits < 0:
            new_digit = diff_of_digits + base
            borrow = 1
        else:
            new_digit = diff_of_digits
            borrow = 0

        result = auxiliary.characters[new_digit] + result

        i -= 1

    # Now we want to check if we have any redundant 0's left in the front of the result and delete them, if there are
    # any.
    redundant_zeroes = 0

    while result[redundant_zeroes] == '0':
        redundant_zeroes += 1
        if redundant_zeroes >= len(result):
            break

    aux_result = result
    result = ""

    # We save only the digits to the right of the redundant 0's.
    while redundant_zeroes < len(aux_result):
        result += aux_result[redundant_zeroes]
        redundant_zeroes += 1

    # If the values were previously swapped then it means that the result should be negative.
    if swapped:
        result = '-' + result

    # If the result string is empty at this point, then it means the result is 0.
    if result == '':
        result = '0'

    # Return the result of the subtraction as a string.
    return result


def multiplication_with_one_digit(number, factor, base):
    """
        This function calculates the product of two numbers in a given base. (One of the is composed by only one digit)

    :param number: String
    :param factor: String (one digit)
    :param base: Integer representing the base in which the two numbers are given.
    :return: String representing the product of the two values.
    """

    # The result of the multiplication will be stored as a string.
    product = ""

    # Extract the decimal value of the digit with which we multiply.
    decimal_factor = auxiliary.characters.index(factor)

    # Check if the first character of the number to be multiplied is '-'.
    negative = False

    # If that's the case, then it means that the number is negative and if we multiply it with a positive digit it means
    # that the result should be negative.
    if number[0] == '-':
        negative = True
        number = number[1:]

    i = len(number) - 1

    # This will store the transport digit.
    carry = 0

    while i >= 0:
        # Convert the current digit to decimal. 
        digit = auxiliary.characters.index(number[i])

        # Multiply the current digit by the factor with which we multiply and add the carry. 
        product_of_digits = digit * decimal_factor + carry

        # Add to the front of the product the newly obtained digit. 
        product = auxiliary.characters[product_of_digits % base] + product

        # Compute the new carry. 
        carry = product_of_digits // base

        i -= 1

    # Check if we have a transport digit. 
    if carry != 0:
        product = auxiliary.characters[carry] + product

    # Check if the result of the multiplication is 0. (Multiplied by 0)
    if product.count('0') == len(product):
        product = '0'

    # Add the minus sign only if the initial number was negative and the result is non-zero. 
    if negative:
        if product != '0':
            product = '-' + product

    return product


def division_by_one_digit(number, divider, base):
    """
        This function calculates the quotient and remainder obtained from the division of a number and a digit.

    :param number: String
    :param factor: String (one digit)
    :param base: Integer representing the base in which the two numbers are given.
    :return: Two strings, the first one being the quotient and the second one being the remainder obtained from the division. 
    """

    # The results obtained from the division will be stored as strings. 
    quotient = ""
    remainder = ""

    first_division = True

    transport = '0'

    # Extract the decimal value from the digit with which we divide. 
    divider_decimal = auxiliary.characters.index(divider)

    for i in range(len(number)):
        # Convert to decimal the transport and the current digit from the number. 
        digit1 = auxiliary.characters.index(transport)
        digit2 = auxiliary.characters.index(number[i])

        # Compute the value that we have to divide. 
        dividend_decimal = digit1 * base + digit2

        if not first_division or dividend_decimal >= divider_decimal:
            # If it is not the first division, then we can add the result to the quotient.
            # This check is done in order to not add redundant zeroes at the front of the result. 

            # Obtain one of the quotient's digits as the quotient obtained from dividing the current value with the divider. 
            quotient += str(auxiliary.characters[dividend_decimal // divider_decimal])

        first_division = False
        
        # Compute the transport digit as the modulus of the current value and the divider.  
        transport = str(auxiliary.characters[dividend_decimal % divider_decimal])

    # The last transport digit is the final remainder. 
    remainder = transport

    # If the quotient is empty, then the result is 0. 
    if quotient == '':
        quotient = '0'

    return quotient, remainder


def successive_divisions_conversion_method(number, initial_base, final_base):
    """
        This function takes as a parameter a string representing a number in a given base and returns a string of the digits of the same number
    represented in a different base.

    This method can be applied only if the initial base is greater than the final base because this way we divide only by a single digit.

    :param number: String which is the representation of a number in a given base.
    :param initial_base: Integer showing the base in which the given number is represented.
    :param final_base: Integer showing the base in which we want to convert the number.
    :return: String of digits composing the number represented in the required base.
    """

    # The divider needs to be a character. (The function for divisions receives the divider as a string)
    divider = auxiliary.characters[final_base]

    # This string will store the result.
    result = ""

    # While the number is not empty, keep dividing and concatenate the remainders to the result string.
    while number != '0':
        number, remainder = division_by_one_digit(number, divider, initial_base)
        result = remainder + result

    # Return the converted number.
    return result


def power(number, exponent, base):
    """
        This function calculates the value of a given number raised to a given power in a certain base.

    :param number: String (a single digit) which is the representation of a number in a given base.
    :param exponent: Integer meaning of how many times do we have to multiply.
    :return: String of digits composing the result of number to the power exponent.
    """

    product = "1"

    # We raise the number to the required power by using the multiplication function. 
    # It is mandatory that the number is a single digit.
    for i in range(exponent):
        product = multiplication_with_one_digit(product, number, base)

    # Return the result
    return product


def substitution_conversion_method(number, initial_base, final_base):
    """
        This function takes as a parameter a string representing a number in a given base and returns a string of the digits of the same number
    represented in a different base.

    This method can be applied only if the initial base is less than the final base because this way we only do multiplications by one digit.

    :param number: String which is the representation of a number in a given base.
    :param initial_base: Integer showing the base in which the given number is represented.
    :param final_base: Integer showing the base in which we want to convert the number.
    :return: String of digits composing the number represented in the required base.
    """

    # This string will contain the result. 
    # We compute the result by adding the products of every digit with the base raised to the corresponding power.
    result = "0"

    # Convert the initial base in the corresponding digit from '2' to 'F'
    initial_base = auxiliary.characters[initial_base]

    for i in range(len(number)):
        # Extract the current digit.
        digit = number[i]

        # Calculate: initial_base ^ position (calculations done in the destination base).
        positional_value = power(initial_base, len(number) - i - 1, final_base)

        # Multiply the previously computed value with the current digit.
        new_term = multiplication_with_one_digit(positional_value, digit, final_base)

        # Then add it to the result.
        result = add_numbers_in_a_base(result, new_term, final_base)

    # Return the number represented in the new base. 
    return result


def rapid_conversions(number, initial_base, final_base):
    """
        This function takes as parameters a number as a string and two bases as integers(2, 4, 8, 16) and performs the conversion of the given 
    value from the initial base to the final base using rapid conversions. 
        It uses base 2 as an intermediate base. 

    :param number: String which is the representation of a number in a given base.
    :param initial_base: Integer showing the base in which the given number is represented.
    :param final_base: Integer showing the base in which we want to convert the number.
    :return: String of digits composing the number represented in the required base.
    """

    # Make sure the number is in binary, then take it to the required base. 

    if initial_base != 2:
        # Convert the number to binary.

        # Use the appropriate table for rapid conversions. 
        table = auxiliary.rapid_conversions_2_4
        if initial_base == 8:
            table = auxiliary.rapid_conversions_2_8
        elif initial_base == 16:
            table = auxiliary.rapid_conversions_2_16
        
        # This string will temporarily store the binary configuration of the given number. 
        number_binary = ""

        for i in range(len(number)):
            digit = auxiliary.characters.index(number[i])

            number_binary += table[digit][0]
        
        # Substitute the number with its binary representation. 
        number = number_binary

    # Now choose the appropriate table and number of digits to convert the number from binary to the final base. 
    required_digits = 2
    table = auxiliary.rapid_conversions_2_4

    if final_base == 8:
        required_digits = 3
        table = auxiliary.rapid_conversions_2_8

    elif final_base == 16:
        required_digits = 4
        table = auxiliary.rapid_conversions_2_16

    # Delete the redundant zeroes from the front of the number.
    while number[0] == '0':
        number = number[1:]

    # Add back some insignificant zeroes to the left of the number, if needed, so that we can make 'groups' of digits of the
    # required length. 
    while len(number) % required_digits != 0:
        number = '0' + number

    # This string will store the final result. 
    result = ""

    for i in range(0, len(number), required_digits):
        # Extract a group of digits of the needed length.
        tuple_of_digits = number[i:i + required_digits]

        corresponding_digits = ""

        for key in table:
            # Look for the corresponding configuration in the table.
            if table[key][0] == tuple_of_digits:
                corresponding_digits = table[key][1]
        
        # Concatenate the corresponding group of digits to the result.
        result += corresponding_digits
    
    # Return the result. 
    return result


"""
    THE FOLLOWING ALGORITHMS ARE USED TO CONVERT NUMBERS INTO DECIMAL OR FROM DECIMAL
"""


def successive_divisions_conversion_from_decimal(number, final_base):
    """
        This function takes an integer in decimal as a parameter and returns as a string the representation of that number
    in a given base.

    :param number: Integer
    :param final_base: Integer
    :return: String which is the representation of the number in the given base.
    """

    # The result will be stored as a string.
    result = ""

    # While the number is non-zero we keep dividing by the base.
    while number != 0:
        # We get the remainder.
        remainder = number % final_base
        # Then we divide the number by the base(integer division).
        number //= final_base

        # And finally, we add the remainder in the front of the result.
        result = auxiliary.characters[remainder] + result

    # Return the result as a string which is the representation of the decimal number in the given base.
    return result


def substitution_method_conversion_to_decimal(number, initial_base):
    """
        This function takes a string as a parameter representing the number given in the initial base and converts it to
    decimal using the substitution method.

    :param number: String which is the representation of a number in a given base.
    :param initial_base: Integer showing the base in which the given number is represented.
    :return: Integer representing the decimal value of the given number.
    """

    # The result will be stored as a string.
    result = 0

    for i in range(len(number)):
        # Calculate the exponent. (The indices in representations are reversed compared to the indices of the characters
        # of a string.
        exponent = len(number) - i - 1

        # We add to the result the decimal value of the digit multiplied by the base raised to the calculated exponent.
        result += auxiliary.characters.index(number[i]) * (initial_base ** exponent)

    # Return the result as a decimal number.
    return result

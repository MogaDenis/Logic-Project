import auxiliary

# TODO - additions(done), subtractions, multiplications and divisions by one digit
# TODO - conversions by successive division, substitution method, rapid conversion


def check_if_valid_base(number, base):
    """
    This function checks if a given number is correctly represented in the given base. (Checks if there are digits that
    are not available in the given base)

    :return: True - if the representation is valid and False, otherwise
    """

    for digit in number:
        if auxiliary.characters.index(digit) >= base:
            return False

    return True


def add_numbers_in_a_base(number1, number2, base):
    """
    This function adds two numbers in a given base from 2 to 16.

    :param number1: String
    :param number2: String
    :param base: Integer representing the base in which are the numbers given.
    :return: String having the digits of the sum of the two numbers in the given base.
    """

    result = ""

    i = len(number1) - 1
    j = len(number2) - 1

    carry = 0

    while i >= 0 and j >= 0:
        digit1 = auxiliary.characters.index(number1[i])
        digit2 = auxiliary.characters.index(number2[j])

        sum_of_digits = digit1 + digit2 + carry

        new_digit = sum_of_digits % base

        result = auxiliary.characters[new_digit] + result

        carry = sum_of_digits // base

        i -= 1
        j -= 1

    while i >= 0:
        digit = auxiliary.characters.index(number1[i])

        sum_of_digits = digit + carry

        new_digit = sum_of_digits % base

        result = auxiliary.characters[new_digit] + result

        carry = sum_of_digits // base

        i -= 1

    while j >= 0:
        digit = auxiliary.characters.index(number2[j])

        sum_of_digits = digit + carry

        new_digit = sum_of_digits % base

        result = auxiliary.characters[new_digit] + result

        carry = sum_of_digits // base

        j -= 1

    if carry != 0:
        result = str(carry) + result

    return result


def successive_divisions_conversion(number, final_base):
    """

    :param number:
    :param final_base:
    :return:
    """

    result = ""
    while number != 0:
        remainder = number % final_base
        number //= final_base
        result = auxiliary.characters[remainder] + result
    return result


def rapid_conversions_method(number, initial_base, final_base):
    """

    :param number:
    :param initial_base:
    :param final_base:
    :return:
    """

    conversions = {
    #   10      2      4      8    16

    }

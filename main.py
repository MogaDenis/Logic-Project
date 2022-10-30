import auxiliary

# TODO - additions(done), subtractions(done), multiplications(done) and divisions by one digit
# TODO - conversions by successive division(almost done), substitution method, rapid conversion


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


def compare(number1, number2, base):
    """

    :param number1:
    :param number2:
    :param base:
    :return:
    """

    if len(number1) < len(number2):
        return True

    elif len(number1) > len(number2):
        return False

    i = 0
    j = 0

    while i < len(number1) and j < len(number2):
        digit1 = auxiliary.characters.index(number1[i])
        digit2 = auxiliary.characters.index(number2[j])

        if digit1 < digit2:
            return True

    return False


def subtract_numbers_in_a_base(number1, number2, base):
    """

    :param number1:
    :param number2:
    :param base:
    :return:
    """

    result = ""
    swapped = False

    if compare(number1, number2, base):
        aux = number1
        number1 = number2
        number2 = aux
        swapped = True

    i = len(number1) - 1
    j = len(number2) - 1

    borrow = 0

    while i >= 0 and j >= 0:
        digit1 = auxiliary.characters.index(number1[i])
        digit2 = auxiliary.characters.index(number2[j])

        diff_of_digits = digit1 - digit2 - borrow

        if diff_of_digits < 0:
            new_digit = diff_of_digits + base
            borrow = 1
        else:
            borrow = 0
            new_digit = diff_of_digits

        result = auxiliary.characters[new_digit] + result

        i -= 1
        j -= 1

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

    while j >= 0:
        digit = auxiliary.characters.index(number1[j])

        diff_of_digits = digit - borrow

        if diff_of_digits < 0:
            new_digit = diff_of_digits + base
            borrow = 1
        else:
            new_digit = diff_of_digits
            borrow = 0

        result = auxiliary.characters[new_digit] + result

        j -= 1

    redundant_zeroes = 0

    while result[redundant_zeroes] == '0':
        redundant_zeroes += 1

    aux_result = result
    result = ""

    while redundant_zeroes < len(aux_result):
        result += aux_result[redundant_zeroes]
        redundant_zeroes += 1

    if swapped:
        result = '-' + result

    return result


def multiplication_with_one_digit(number, factor, base):
    """

    :param number:
    :param factor:
    :param base:
    :return:
    """

    product = ""

    decimal_factor = auxiliary.characters.index(factor)

    negative = False

    if number[0] == '-':
        negative = True
        number = number[1:]

    i = len(number) - 1

    carry = 0

    while i >= 0:
        digit = auxiliary.characters.index(number[i])

        product_of_digits = digit * decimal_factor + carry

        product = auxiliary.characters[product_of_digits % base] + product

        carry = product_of_digits // base

        i -= 1

    if carry != 0:
        product = auxiliary.characters[carry] + product

    if negative:
        product = '-' + product

    return product


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

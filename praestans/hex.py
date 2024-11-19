from praestans.dec import decimal_to_binray
from praestans.bin import binary_to_octal
from praestans.err import error_handling

@error_handling
def hexa_to_decimal(number):
    """
    Converts a hexadecimal (base-16) number to its decimal (base-10) representation.

    Parameters:
        number (int | str): The hexadecimal number to convert.

    Returns:
        int: An integer representing the decimal equivalent of the input number.

    Example:
        hexa_to_decimal(ACC342) -> 11322178

    How it works:
        Each digit of the number is multiplied by the power of 16, and these values are summed to obtain the decimal number.
        Starting from rightmost digit, the value of each digit is multiplied by increasing powers of 16, such as 16^0, 16^1 16^2, and so on.
    """
    result = 0
    hexa_str = str(number)
    hexa_chrs_up = "ABCDEF"
    hexa_chrs_low = "abcdef"
    for i in range(len(hexa_str)):
        char = hexa_str[len(hexa_str) - 1 - i]
        if char.isdigit():
            value = int(char)
        elif char in hexa_chrs_up:
            value = 10 + hexa_chrs_up.index(char)
        elif char in hexa_chrs_low:
            value = 10 + hexa_chrs_low.index(char)
        result += value * (16 ** i)
    return (result)


@error_handling
def hexa_to_octal(number):
    """
    Converts a hexadecimal (base-16) number to its octal (base-8) representation.

    Parameters:
        number (int | str): The hexadecimal number to convert.

    Returns:
        int: An integer representing the octal equivalent of the input number.

    Example:
        hexa_to_octal(ab444) -> 2532104

    How it works:
        To convert a hexadecimal number to octal, convert each hexadecimal digit to its 4-bit binary equivalent. 
        Split the binary number into 3-bit groups and convert each group to octal.
    """
    hexa_str = str(number)
    decimal = hexa_to_decimal(hexa_str)
    binary = decimal_to_binray(decimal)
    while len(binary) % 4 != 0:
        binary = "0" + binary
    octal = binary_to_octal(binary)
    return (octal)


@error_handling
def hexa_to_binary(number):
    """
    Converts a hexadecimal (base-16) number to its binary (base-2) representation.

    Parameters:
        number (int | str): The hexadecimal number to convert.

    Returns:
        int: An integer representing the binary equivalent of the input number.

    Example:
        hexa_to_binary(ee324) -> 11101110001100100100

    How it works:
        Convert each hexadecimal digit to its 4-bit binary equivalent. 
        Then, combine these 4-bit binary values to form the binary number.
    """
    hexa_str = str(number)
    decimal = hexa_to_decimal(hexa_str)
    binary = decimal_to_binray(decimal)

    i = 0
    while (hexa_str[i] == "0"):
        i += 1
    j  = 0
    while j < (i * 4):
        binary = "0" + binary
        j += 1
    while len(binary) % 4 != 0:
        binary = "0" + binary
    return (int(binary))

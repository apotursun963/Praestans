from praestans.dec import decimal_to_binray
from praestans.bin import binary_to_hexa
from praestans.err import error_handling

@error_handling
def octal_to_binary(number):
    """
    Converts a octal (base-8) number to its binary (base-2) representation.

    Parameters:
        number (int | str): The octal number to convert.

    Returns:
        int: An integer representing the binary equivalent of the input number.

    Example:
        octal_to_binary(13) -> 1011

    How it works:
        To convert an octal number to binary, convert each octal digit to its 3-bit binary equivalent. 
        If the binary equivalent has less than 3 bits, add leading zeros. Finally, combine these 3-bit values to form the binary number.
    """
    bin_str = ""
    oct_str = str(number)
    for i in range(len(oct_str)):
        part = str(decimal_to_binray(int(oct_str[i])))
        while len(part) < 3:
            part = "0" + part
        bin_str += part
    return (int(bin_str.lstrip("0") or "0"))


@error_handling
def octal_to_decimal(number):
    """
    Converts a octal (base-8) number to its decimal (base-10) representation.

    Parameters:
        number (int | str): The octal number to convert.

    Returns:
        int: An integer representing the decimal equivalent of the input number.

    Example:
        octal_to_decimal(735) -> 477

    How it works:
        Each digit of the number is multiplied by the power of 8, and these values are summed to obtain the decimal number.
        Starting from rightmost digit, the value of each digit is multiplied by increasing powers of 8, such as 8^0, 8^1 8^2, and so on.
    """
    result = 0
    oct_str = str(number)
    for i in range(len(oct_str)):
        result += int(oct_str[len(oct_str) - 1 - i]) * (8 ** i)
    return (result)


@error_handling
def octal_to_hexa(number):
    """
    Converts a octal (base-8) number to its hexadecimal (base-16) representation.

    Parameters:
        number (int | str): The octal number to convert.

    Returns:
        str: A string representing the hexadecimal equivalent of the input number.

    Example:
        octal_to_hexa(3242) -> 6A2

    How it works:
        To convert an octal number to binary, convert each octal digit to its 3-bit binary equivalent. 
        Then, combine these 3-bit values to form the binary number. 
        After that, divide the binary number into 4-bit groups and convert each group to hexadecimal.
    """
    bin_str = octal_to_binary(number)
    hexa_str = binary_to_hexa(bin_str).lstrip("0")
    return (hexa_str)

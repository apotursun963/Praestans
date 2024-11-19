from praestans.err import error_handling

@error_handling
def binary_to_decimal(number):
    """
    Converts a binary (base-2) number to its decimal (base-10) representation.

    Parameters:
        number (int | str): The binary number to convert.

    Returns:
        int: An integer representing the decimal equivalent of the input number.

    Example:
        binary_to_decimal(10011) -> 19

    How it works:
        Each digit of the number is multiplied by the power of 2, and these values are summed to obtain the decimal number.
        Starting from rightmost digit, the value of each digit is multiplied by increasing powers of 2, such as 2^0, 2^1 2^2, and so on.
    """
    result = 0
    binary_str = str(number)
    for i in range(len(binary_str)):
        result += int(binary_str[len(binary_str) - 1 - i]) * (2 ** i)
    return (result)


@error_handling
def binary_to_octal(number):
    """
    Converts a binary (base-2) number to its octal (base-8) representation.

    Parameters:
        number (int | str): The binary number to convert.

    Returns:
        int: An integer representing the octal equivalent of the input number.

    Example:
        binary_to_octal(11101) -> 35

    How it works:
        To convert a binary number to an octal number, we first divide the number into 3-bit groups. 
        If the last group is incomplete, we add leading zeros. 
        For each group, we multiply each digit by the corresponding power of 2, sum these products, and then obtain the octal number. 
        Finally, we combine the octal equivalents of each group.
    """
    octal_str = ""
    binary_str = str(number)

    while len(binary_str) % 3 != 0:
        binary_str = "0" + binary_str

    for i in range(0, len(binary_str), 3):
        group = binary_str[i: i+3]
        result = 0
        for j in range(len(group)):
            result += int(group[len(group) - 1 - j]) * (2 ** j)
        octal_str += str(result)
    return (int(octal_str))


@error_handling
def binary_to_hexa(number):
    """
    Converts a binary (base-2) number to its hexadecimal (base-16) representation.

    Parameters:
        number (int | str): The binary number to convert.

    Returns:
        str: A string representing the hexadecimal equivalent of the input number.

    Example:
        binary_to_hexa(1001011) -> 4B

    How it works:
        To convert a binary number to an hexadecimal number, we first divide the number into 4-bit groups. 
        If the last group is incomplete, we add leading zeros. 
        For each group, we multiply each digit by the corresponding power of 2, sum these products, and then obtain the hexadecimal number. 
        Finally, we combine the hexadecimal equivalents of each group.
    """
    hexa_str = ""
    binary_str = str(number)
    hex_chrs = "0123456789ABCDEF"

    while len(binary_str) % 4 != 0:
        binary_str = "0" + binary_str
    
    for i in range(0, len(binary_str), 4):
        group = binary_str[i: i+4]
        result = 0
        for j in range(len(group)):
            result += int(group[len(group) - 1 - j]) * (2 ** j)
        hexa_str += str(hex_chrs[result])
    return (hexa_str)

from praestans.err import error_handling

@error_handling
def decimal_to_binray(number):
    """
    Converts a decimal (base-10) number to its binary (base-2) representation.

    Parameters:
        number (int | str): The decimal number to convert.

    Returns:
        int: An integer representing the binary equivalent of the input number.

    Example:
        decimal_to_binary(11) -> 1011

    How it works:
        Divide the number by 2 until it becomes 0, and recod the remainder at each step.
        Reverse the remainders to obtain the binary number.
    """
    binary_str = ""
    number = int(number)
    while (number > 0):
        left = number % 2
        number = number // 2
        binary_str += str(left)
    return (int(binary_str[::-1]))


@error_handling
def decimal_to_octal(number):
    octal_str = ""
    number = int(number)
    while (number > 0):
        left = number % 8
        number = number // 8
        octal_str += str(left)
    return (int(octal_str[::-1]))


@error_handling
def decimal_to_hexa(number, size):
    hex_str = ""
    hex_chrs = "0123456789abcdef"
    hex_chrs = hex_chrs.upper() if size == "X" else hex_chrs
    number = int(number)
    while (number > 0):
        left = number % 16
        number = number // 16
        hex_str += hex_chrs[left]
    return (hex_str[::-1])

from praestans.dec import decimal_to_binray
from praestans.bin import binary_to_hexa
from praestans.err import error_handling

# octal -> (binary, decimal, hexadecimal)


@error_handling
def octal_to_binary(number):
    octal_str = str(number)
    binary_str = ""
    for i in range(len(octal_str)):
        part = str(decimal_to_binray(int(octal_str[i])))
        while len(part) < 3:
            part = "0" + part
        binary_str += part
    return (binary_str.lstrip("0") or "0")


@error_handling
def octal_to_decimal(number):
    octal_str = str(number)
    decimal_sum = 0
    for i in range(len(octal_str)):
        decimal_sum += int(octal_str[len(octal_str) - 1 - i]) * (8 ** i)
    return (decimal_sum)


@error_handling
def octal_to_hexa(number):
    binar_str = octal_to_binary(number)
    hexa_str = binary_to_hexa(binar_str).lstrip("0")
    return (hexa_str)

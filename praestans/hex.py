from praestans.dec import decimal_to_binray
from praestans.bin import binary_to_octal
from praestans.err import error_handling

# hexadecimal -> (decimal, octal, binary)


@error_handling
def hexa_to_decimal(number):
    hexa_chrs_up = "ABCDEF"
    hexa_chrs_low = "abcdef"
    hexa_str = str(number)
    dec_sum = 0

    for i in range(len(hexa_str)):
        char = hexa_str[len(hexa_str) - 1 - i]
        if char.isdigit():
            value = int(char)
        elif char in hexa_chrs_up:
            value = 10 + hexa_chrs_up.index(char)
        elif char in hexa_chrs_low:
            value = 10 + hexa_chrs_low.index(char)
        dec_sum += value * (16 ** i)
    return (dec_sum)


@error_handling
def hexa_to_octal(number):
    hexa_str = str(number)
    decimal = hexa_to_decimal(hexa_str)
    binary = decimal_to_binray(decimal)
    while len(binary) % 4 != 0:
        binary = "0" + binary
    octal = binary_to_octal(binary)
    return (octal)


@error_handling
def hexa_to_binary(number):
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
    return (binary)

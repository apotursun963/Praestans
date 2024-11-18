
from praestans.dec import decimal_to_binray
from praestans.bin import binary_to_octal
from praestans.err import error_handling

# hexadecimal -> (decimal, octal, binary)

# hexa to decimal
# sayının her bir basamağı 16'nın üsü olarak temsil edililir.

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


# hexa to octal
# Hexadecimal sayıyı önce 4 bitlik gruplar halinde ikili sayıya çevirin, ardından bu ikili sayıyı 
# 3 bitlik gruplar halinde oktal sayıya dönüştürün. Eğer gerekirse, en sola 0 ekleyerek bit sayısını tamamlayın.

@error_handling
def hexa_to_octal(number):
    hexa_str = str(number)
    decimal = hexa_to_decimal(hexa_str)
    binary = decimal_to_binray(decimal)
    while len(binary) % 4 != 0:
        binary = "0" + binary
    octal = binary_to_octal(binary)
    return (octal)

# hexa to binary
# Hexadecimal sayıyı ikiliye (binary) çevirmek için her bir hexadecimal basamağı, 
# 4 bitlik ikili karşılığına çevirin.

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

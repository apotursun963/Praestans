
from praestans.err import error_handling

# binary -> (decimal, octal, hexadecimal)


# binary to decimal
# sayının her bir basamaığını 2'nin üsünü alıyoruz ve hepsini topluyoruz

@error_handling
def binary_to_decimal(number):
    decimal_str = str(number)
    merge = 0
    for i in range(len(decimal_str)):
        merge += int(decimal_str[len(decimal_str) - 1 - i]) * (2 ** i)
    return (int(merge))


# binary to octal
# İkili sayıyı 3 bitlik gruplara ayırırız. Eğer grup 3 bitten eksikse, başına sıfır ekleriz. 
# Her grubu ikili sistemden oktal sisteme dönüştürüp, sonuçları birleştiririz.

@error_handling
def binary_to_octal(number):
    binary_str = str(number)
    octal_str = ""

    while len(binary_str) % 3 != 0:
        binary_str = "0" + binary_str

    for i in range(0, len(binary_str), 3):
        group = binary_str[i: i+3]
        merge = 0
        for j in range(len(group)):
            merge += int(group[len(group) - 1 - j]) * (2 ** j)
        octal_str += str(merge)
    return (int(octal_str))


# binary to hexadecimal
# Binary sayıyı 4 bitlik gruplara ayırın ve eksik grup varsa başına sıfır ekleyin.
# Her 4 bitlik grubu hexadecimal karşılığına çevirin.

@error_handling
def binary_to_hexa(number):
    hex_chrs = "0123456789ABCDEF"
    binary_str = str(number)
    hexa_str = ""

    while len(binary_str) % 4 != 0:
        binary_str = "0" + binary_str
    
    for i in range(0, len(binary_str), 4):
        group = binary_str[i: i+4]
        merge = 0
        for j in range(len(group)):
            merge += int(group[len(group) - 1 - j]) * (2 ** j)
        hexa_str += str(hex_chrs[merge])
    return (hexa_str)

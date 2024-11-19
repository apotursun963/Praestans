from praestans.err import error_handling


@error_handling
def binary_to_decimal(number):
    
    
    merge = 0
    decimal_str = str(number)
    for i in range(len(decimal_str)):
        merge += int(decimal_str[len(decimal_str) - 1 - i]) * (2 ** i)
    return (int(merge))


@error_handling
def binary_to_octal(number):
    octal_str = ""
    binary_str = str(number)

    while len(binary_str) % 3 != 0:
        binary_str = "0" + binary_str

    for i in range(0, len(binary_str), 3):
        group = binary_str[i: i+3]
        merge = 0
        for j in range(len(group)):
            merge += int(group[len(group) - 1 - j]) * (2 ** j)
        octal_str += str(merge)
    return (int(octal_str))


@error_handling
def binary_to_hexa(number):
    hexa_str = ""
    binary_str = str(number)
    hex_chrs = "0123456789ABCDEF"

    while len(binary_str) % 4 != 0:
        binary_str = "0" + binary_str
    
    for i in range(0, len(binary_str), 4):
        group = binary_str[i: i+4]
        merge = 0
        for j in range(len(group)):
            merge += int(group[len(group) - 1 - j]) * (2 ** j)
        hexa_str += str(hex_chrs[merge])
    return (hexa_str)

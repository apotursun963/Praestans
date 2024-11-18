
def verify_input(params, characters):
    if not isinstance(params, (str, int)):
        raise TypeError("input value must be of type string or integer.")
    if not params:
        raise ValueError("input value cannot be empty")
    for chr in str(params):
        if chr not in characters:
            raise ValueError(f"input value must contain only allowed characters: {characters}")

def error_handling(func):
    def wrapper(*args, **kwargs):
        params = args[0]
        binary_chrs = ("0", "1")
        octal_chrs = ("0", "1", "2", "3", "4", "5", "6", "7")
        decimal_chrs = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        hexa_chrs = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F")
    
        FT_BINARY = ["binary_to_decimal", "binary_to_octal", "binary_to_hexa"]
        FT_OCTAL = ["octal_to_binary", "octal_to_decimal", "octal_to_hexa"]
        FT_DECIMAL = ["decimal_to_binary", "decimal_to_octal", "decimal_to_hexa"]
        FT_HEXAD = ["hexa_to_decimal", "hexa_to_octal", "hexa_to_binary"]

        if func.__name__ in FT_BINARY:
            verify_input(params, binary_chrs)
        elif func.__name__ in FT_OCTAL:
            verify_input(params, octal_chrs)
        elif func.__name__ in FT_DECIMAL:
            verify_input(params, decimal_chrs)
        elif func.__name__ in FT_HEXAD:
            verify_input(params, hexa_chrs)

        result = func(*args, **kwargs)
        return (result)
    return (wrapper)

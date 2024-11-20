praestans
----------

![veni2](https://github.com/user-attachments/assets/0e6e7ab9-7f72-470a-91a3-3b12860455d9)

This Python library allows you to easily convert between binary, octal, decimal, and hexadecimal number systems. 
You can perform conversions between different number systems quickly and accurately.
Whether you're doing basic calculations or working on software projects that involve numbers, this library saves you time. 
It's an ideal tool for those looking for a simple and effective solution.

  - PyPI: https://pypi.org/project/praestans
  - Source code: https://github.com/apotursun963/praestans

Installation
------------
```
pip install praestans
```

Example usage
-------------
This library offers a total of 12 different functions to convert between binary, octal, decimal, and hexadecimal number systems. 
Here are 4 examples of these functions:
```python
from praestans.bin import binary_to_decimal
from praestans.dec import decimal_to_hexa
from praestans.oct import octal_to_decimal
from praestans.hex import hexa_to_binary


# Conversion from binary to decimal
binary = 1011
decimal_res = binary_to_decimal(binary)
print(f"binary: {binary} -> decimal: {decimal_res}")


# Conversion from octal to decimal
octal = 1771
decimal_res = octal_to_decimal(octal)
print(f"octal: {octal} -> decimal: {decimal_res}")


# Conversion from decimal to hexa
decimal = 255
hexa_res = decimal_to_hexa(decimal, "X")
print(f"decimal: {decimal} -> hexadecimal: {hexa_res}")


# Conversion from hexa to binary
hexa = "AE221"
binary_res = hexa_to_binary(hexa)
print(f"hexa: {hexa} -> binary: {binary_res}")
```

Project Structure
------------------
```
praestans/
├── praestans/                    # Main Python module (same name as the project)
│   ├── __init__.py               # Package initializer file
│   ├── bin.py
│   ├── dec.py
│   ├── err.py
│   ├── hex.py
│   ├── oct.py
├── ceaser.jpg                    # Image file
├── LICENSE                       # License information
├── README.md                     # Project description
├── setup.py                      # Script for package installation
└── test.py                       # Test file
```

Running test
------------
```
python .\test.py
```

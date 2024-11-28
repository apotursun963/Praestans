# Praestans: A Simple and Efficient Number System Converter

![Version](https://img.shields.io/badge/version-0.1.2-orange)  
![License](https://img.shields.io/badge/license-MIT-green)  
![Top Language](https://img.shields.io/github/languages/top/apotursun963/praestans)  
![Build Status](https://img.shields.io/github/workflow/status/apotursun963/praestans/build)  
![Last Commit](https://img.shields.io/github/last-commit/apotursun963/praestans)

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Example Usage](#example-usage)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Introduction
**Praestans** is a Python library designed to simplify the conversion between binary, octal, decimal, and hexadecimal number systems. Whether you're doing basic calculations or working on more complex software projects, this library offers an efficient and accurate solution for number system conversions. It is an ideal tool for anyone who needs fast and reliable conversions between different numeric systems.

## Installation
You can install **Praestans** using `pip`:
```bash
pip install praestans


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

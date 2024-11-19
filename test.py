from praestans.bin import *
from praestans.oct import *
from praestans.dec import *
from praestans.hex import *
import unittest

class TestNumberSystem(unittest.TestCase):

    # ---------------------- BINARY TEST --------------------

    def test_bin2dec(self): 
        self.assertEqual(binary_to_decimal(1011), 11)
        self.assertEqual(binary_to_decimal("11011"), 27)
        self.assertEqual(binary_to_decimal(111101), 61)
        self.assertEqual(binary_to_decimal("0001"), 1)
        self.assertEqual(binary_to_decimal(11111111111), 2047)

    def test_bin2oct(self):
        self.assertEqual(binary_to_octal(10111), 27)
        self.assertEqual(binary_to_octal("10101011"), 253)
        self.assertEqual(binary_to_octal(1000000), 100)
        self.assertEqual(binary_to_octal("0011"), 3)
        self.assertEqual(binary_to_octal(11110101001), 3651)

    def test_bin2hex(self):
        self.assertEqual(binary_to_hexa(100111), "27")
        self.assertEqual(binary_to_hexa("10101011"), "AB")
        self.assertEqual(binary_to_hexa(111100011), "1E3")
        self.assertEqual(binary_to_hexa("011"), "3")
        self.assertEqual(binary_to_hexa(11111101), "FD")

    # ---------------------- OCTAL TEST -----------------------

    def test_oct2dec(self):
        self.assertEqual(octal_to_decimal(535), 349)
        self.assertEqual(octal_to_decimal("75634"), 31644)
        self.assertEqual(octal_to_decimal(11123), 4691)
        self.assertEqual(octal_to_decimal("0234234"), 80028)
        self.assertEqual(octal_to_decimal(10272), 4282)

    def test_oct2bin(self):
        self.assertEqual(octal_to_binary(26), 10110)
        self.assertEqual(octal_to_binary("7623"), 111110010011)
        self.assertEqual(octal_to_binary(12312311), 1010011001010011001001)
        self.assertEqual(octal_to_binary("01234"), 1010011100)
        self.assertEqual(octal_to_binary(712635), 111001010110011101)

    def test_oct2hex(self):
        self.assertEqual(octal_to_hexa(53), "2B")
        self.assertEqual(octal_to_hexa("1252"), "2AA")
        self.assertEqual(octal_to_hexa(13224), "1694")
        self.assertEqual(octal_to_hexa("7033"), "E1B")
        self.assertEqual(octal_to_hexa(777771), "3FFF9")

    # ---------------------- DECIMAL TEST -----------------------

    def test_dec2bin(self):
        self.assertEqual(decimal_to_binray(982), "1111010110")
        self.assertEqual(decimal_to_binray("28330"), "110111010101010")
        self.assertEqual(decimal_to_binray(11092), "10101101010100")
        self.assertEqual(decimal_to_binray("0234"), "11101010")
        self.assertEqual(decimal_to_binray(234213), "111001001011100101")

    def test_dec2oct(self):
        self.assertEqual(decimal_to_octal(10), 12)
        self.assertEqual(decimal_to_octal("723"), 1323)
        self.assertEqual(decimal_to_octal(1311), 2437)
        self.assertEqual(decimal_to_octal("0281"), 431)
        self.assertEqual(decimal_to_octal(712213635), 5234702203)

    def test_dec2hex(self):
        self.assertEqual(decimal_to_hexa(13, "x"), "d")
        self.assertEqual(decimal_to_hexa("89247", "X"), "15C9F")
        self.assertEqual(decimal_to_hexa(981, "X"), "3D5")
        self.assertEqual(decimal_to_hexa("00014", "x"), "e")
        self.assertEqual(decimal_to_hexa(1110113, "X"), "10F061")
    
    # ---------------------- HEXDECIMAL TEST -----------------------

    def test_hex2bin(self):
        self.assertEqual(hexa_to_binary("abd3"), "1010101111010011")
        self.assertEqual(hexa_to_binary(123), "000100100011")
        self.assertEqual(hexa_to_binary("efab"), "1110111110101011")
        self.assertEqual(hexa_to_binary("0817A"), "00001000000101111010")
        self.assertEqual(hexa_to_binary("0123456789abcdef"), "0000000100100011010001010110011110001001101010111100110111101111")

    def test_hex2oct(self):
        self.assertEqual(hexa_to_octal(93), 223)
        self.assertEqual(hexa_to_octal("aaa3"), 125243)
        self.assertEqual(hexa_to_octal("BEDD"), 137335)
        self.assertEqual(hexa_to_octal("0281A"), 24032)
        self.assertEqual(hexa_to_octal(323023), 14430043)

    def test_hex2dec(self):
        self.assertEqual(hexa_to_decimal("eff234"), 15725108)
        self.assertEqual(hexa_to_decimal("7334E"), 471886)
        self.assertEqual(hexa_to_decimal(1234), 4660)
        self.assertEqual(hexa_to_decimal("000ee"), 238)
        self.assertEqual(hexa_to_decimal("0123456789"), 4886718345)


if __name__ == "__main__":
    unittest.main()

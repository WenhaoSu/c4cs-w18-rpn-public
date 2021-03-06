import unittest
import rpn
from colorama import Fore, Style

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_pow(self):
        result = rpn.calculate("3 3 ^")
        self.assertEqual(27, result)
    def test_error_parameter(self):
        result = rpn.calculate("3 3 / 1")
        self.assertEqual(Fore.RED + "Too many parameter" + Style.RESET_ALL, result)
    def test_error_operator(self):
        result = rpn.calculate("3 3 @")
        self.assertEqual(Fore.RED + "Invalid operator" + Style.RESET_ALL, result)


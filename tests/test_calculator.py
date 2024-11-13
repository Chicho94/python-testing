import unittest
from src.calculator import add, substract, multiply, divide

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        assert add(2,3) == 5

    def test_substract(self):
        assert substract(10,3) == 7

    def test_multiply(self):
        assert multiply(10,3) == 30

    def test_divide(self):
        self.assertRaises(ValueError,divide,10,0)
        # assert divide(10,2) == 5

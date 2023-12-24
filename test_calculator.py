import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        calculator = Calculator()
        result = calculator.add(3,7)
        self.assertEqual(result,10)

    def test_subtraction(self):
        calculator = Calculator()
        result = calculator.subtract(10,4)
        self.assertEqual(result,6)

    def test_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(5,2)
        self.assertEqual(result, 10)

    def test_division(self):
        calculator = Calculator()
        result = calculator.divide(8,4)
        self.assertEqual(result,2)

    def test_division_by_zero(self):
        calculator = Calculator()
        with self.assertRaises(ValueError):
            calculator.divide(10,0)



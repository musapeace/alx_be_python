import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def test_addition(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtraction(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_multiplication(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_division(self):
        calc = SimpleCalculator()
        self.assertEqual(self.calc.divide(10, 2), 5.0) 
        self.assertIsNone(self.calc.divide(7, 0)) 

if __name__ == '__main__':
    unittest.main()
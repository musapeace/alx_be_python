import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.add(2, 3), 5)

    def test_subtract(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.subtract(5, 2), 3)

    def test_multiply(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.multiply(3, 4), 12)

    def test_divide(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.divide(10, 2), 5.0) 
        self.assertIsNone(calc.divide(7, 0)) 

if __name__ == '__main__':
    unittest.main()
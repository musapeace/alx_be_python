import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        self.calc = SimpleCalculator(2, 3)
        self.assertEqual(self.calc.add(), 5, 'Error')

    def test_subtract(self):
        self.calc = SimpleCalculator(5, 2)
        self.assertEqual(self.calc.subtract(), 3)

    def test_multiply(self):
        self.calc = SimpleCalculator(3, 4)
        self.assertEqual(self.calc.multiply(), 12)

    def test_divide(self):
        self.calc = SimpleCalculator(10, 2)
        self.assertEqual(self.calc.divide(), 5.0) 
         

if __name__ == '__main__':
    unittest.main()
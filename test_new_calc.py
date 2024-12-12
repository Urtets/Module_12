import unittest
import calculator_1

class NewCalcTest(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(calculator_1.sqrt(4), 2)

    def test_pow(self):
        self.assertEqual(calculator_1.pow(3, 3), 27)
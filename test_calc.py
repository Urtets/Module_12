import calculator_1
import unittest

class CalcTest(unittest.TestCase):
    def test_add(self):
        """Test to add function in calculator_1
        :return
        """
        self.assertEqual(calculator_1.add(1, 2), 3)
    def test_sub(self):
        self.assertEqual(calculator_1.sub(5, 3), 2)


if __name__ == "__main__":
    unittest.main()
import random

import calculator_1
import unittest


class CalcTest(unittest.TestCase):

    def setUp(self):
        print("Setup")

    @classmethod
    def setUpClass(cls):
        print("MegaSetup")

    def tearDown(self):
        print("Finished function")

    @classmethod
    def tearDownClass(cls):
        print("Finished class")

    @unittest.skip("Не требуется для конкретной задачи")
    def test_add(self):
        """Test to add function in calculator_1
        :return
        """
        self.assertEqual(calculator_1.add(1, 2), 3)

    @unittest.skipIf(random.randint(0, 2), "Не повезло")
    def test_sub(self):
        self.assertEqual(calculator_1.sub(5, 3), 2)

    def test_test(self):
        self.assertIn('g', 'gemini')

    def test_mul(self):
        self.assertEqual(calculator_1.mul(2, 5), 10)

    def test_div(self):
        self.assertEqual(calculator_1.div(10, 2), 5)


if __name__ == "__main__":
    unittest.main()

import calculator_1
import unittest


class CalcTest(unittest.TestCase):

    def setUp(self):
        print("Setup")

    @classmethod
    def setUpClass(cls):
        print("MegaSetup")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_add(self):
        """Test to add function in calculator_1
        :return
        """
        self.assertEqual(calculator_1.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(calculator_1.sub(5, 3), 2)

    def test_test(self):
        self.assertIn('b', 'gemini')

if __name__ == "__main__":
    unittest.main()

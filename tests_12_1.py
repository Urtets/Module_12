import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        kolya_runner = Runner("Коля")
        for _ in range(10):
            kolya_runner.walk()
        self.assertEqual(kolya_runner.distance, 50)


    def test_run(self):
        kolya_runner = Runner("Коля")
        for _ in range(10):
            kolya_runner.run()
        self.assertEqual(kolya_runner.distance, 100)


    def test_challenge(self):
        kolya_runner = Runner("Коля")
        petya_runner = Runner("Петя")
        for _ in range(10):
            kolya_runner.run()
            petya_runner.walk()
        self.assertNotEqual(kolya_runner.distance, petya_runner.distance)



if __name__ == "__main__":
    unittest.main()
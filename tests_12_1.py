import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed


    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest(unittest.TestCase):
    is_frozen = False
    def test_walk(self):
        kolya_runner = Runner("Коля")
        for _ in range(10):
            kolya_runner.walk()
        self.assertEqual(kolya_runner.distance, 50)


    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
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

    import doctest

    doctest.testmod()
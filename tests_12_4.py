import unittest
import logging


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


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        try:

            kolya_runner = Runner("Коля", -1)
            for _ in range(10):
                kolya_runner.walk()
            self.assertEqual(kolya_runner.distance, 50)
            logging.info("\"test_walk\" выполнен успешно")
        except ValueError as exc:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    # @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            kolya_runner = Runner(2)
            for _ in range(10):
                kolya_runner.run()
            self.assertEqual(kolya_runner.distance, 100)
            logging.info("\"test_run\" выполнен успешно")
        except TypeError as exc:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        kolya_runner = Runner("Коля")
        petya_runner = Runner("Петя")
        for _ in range(10):
            kolya_runner.run()
            petya_runner.walk()
        self.assertNotEqual(kolya_runner.distance, petya_runner.distance)


if __name__ == "__main__":
    # unittest.main()
    logging.basicConfig(level=logging.WARNING, filemode='w', filename="runner_tests.log",
                        encoding='UTF-8', format="%(levelname)s | %(message)s | %(asctime)s",
                        datefmt='%d/%m/%Y %I:%M:%S %p')

#     first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())
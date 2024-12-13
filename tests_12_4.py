import logging
import unittest

from tests_12_1 import Runner

logging.basicConfig(level=logging.WARNING, filemode='w', filename='runner_tests.log',
                    encoding='UTF-8', format="%(levelname)s | %(message)s | %(asctime)s")


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):

        try:
            kolya_runner = Runner("Коля", -1)
            for _ in range(10):
                kolya_runner.walk()
            self.assertEqual(kolya_runner.distance, 50)
            logging.info("\"test_walk\" выполнен успешно")
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    # @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            kolya_runner = Runner(2)
            for _ in range(10):
                kolya_runner.run()
            self.assertEqual(kolya_runner.distance, 100)
            logging.info("\"test_run\" выполнен успешно")
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        kolya_runner = Runner("Коля")
        petya_runner = Runner("Петя")
        for _ in range(10):
            kolya_runner.run()
            petya_runner.walk()
        self.assertNotEqual(kolya_runner.distance, petya_runner.distance)


if __name__ == "__main__":
    unittest.main()



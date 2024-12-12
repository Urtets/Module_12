import unittest
from tests_12_2 import TournamentTest
from tests_12_1 import RunnerTest

suite_checker = unittest.TestSuite()
suite_checker.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
suite_checker.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))

running_unit = unittest.TextTestRunner(verbosity=2)
running_unit.run(suite_checker)
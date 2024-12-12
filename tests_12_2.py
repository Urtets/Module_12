import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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

                if self.full_distance < (participant.speed*2) * 2:
                    participant.speed = participant.speed * 0.1
                participant.run()
                # print(participant.distance, participant.name)
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)


        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner('Usain', 10)
        self.runner_andrew = Runner('Andrew', 9)
        self.runner_nick = Runner('Nick', 3)

    @classmethod
    def tearDownClass(cls):
        for runner in cls.all_results:
            print(f'{runner}')

    def test_usain_nick(self):
        tour_1 = Tournament(90, self.runner_nick, self.runner_usain)
        TournamentTest.all_results = tour_1.start()
        self.assertTrue('Nick' == self.all_results[len(self.all_results)].name)
        print(self.all_results[1].name)

    @unittest.skipIf(is_frozen == True, "Не тестируем")
    def test_andrew_nick(self):
        tour_1 = Tournament(90, self.runner_andrew, self.runner_nick)
        self.all_results = tour_1.start()
        self.assertTrue('Nick' == self.all_results[len(self.all_results)].name)

    def test_usain_andrew_nick(self):
        tour_1 = Tournament(1, self.runner_nick, self.runner_usain, self.runner_andrew)
        self.all_results = tour_1.start()
        self.assertTrue('Nick' == self.all_results[len(self.all_results)].name)
        print(self.all_results[1].name)

if __name__ == '__main__':
    unittest.main()

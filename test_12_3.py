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
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, '')
    def test_walk(self):
        runn = Runner('pp')
        step = 10
        while step != 0:
            runn.walk()
            step -= 1

        self.assertEqual(runn.distance, 50)

    @unittest.skipIf(is_frozen, '')
    def test_run(self):
        runn_2 = Runner('ppt')
        step = 10
        while step != 0:
            runn_2.run()
            step -= 1

        self.assertEqual(runn_2.distance, 100)

    @unittest.skipIf(is_frozen, '')
    def test_challenge(self):
        challenge = Runner('pp')
        challenge_2 = Runner('ppt')
        step = 10
        while step != 0:
            challenge.run()
            challenge_2.walk()
            step -= 1

        step = 10


        self.assertNotEqual(challenge.distance, challenge_2.distance)


class TournamentTest(unittest.TestCase):
    all_results = {}
    is_frozen = True

    def setUp(self):
        self.runner1 = Runner(name="Усэйн", speed=10)
        self.runner2 = Runner(name="Андрей", speed=9)
        self.runner3 = Runner(name="Ник", speed=3)


    def tearDown(self):
        for key in sorted(self.all_results.keys()):
            print(f"{key}: {self.all_results[key]}  ")
        # print(self.all_results[1])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_runner = max(self.all_results.keys())
        self.assertTrue(self.all_results[last_runner] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_runner = max(self.all_results.keys())
        self.assertTrue(self.all_results[last_runner] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_runner = max(self.all_results.keys())
        self.assertTrue(self.all_results[last_runner] == "Ник")

if __name__ == '__main__':
    unittest.main()
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
        runn = Runner('pp')
        step = 10
        while step != 0:
            runn.walk()
            step -= 1

        self.assertEqual(runn.distance, 50)

    def test_run(self):
        runn_2 = Runner('ppt')
        step = 10
        while step != 0:
            runn_2.run()
            step -= 1

        self.assertEqual(runn_2.distance, 100)

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

if __name__ == '__main__':
    unittest.main()
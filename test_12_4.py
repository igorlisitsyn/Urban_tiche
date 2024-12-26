import unittest
import logging

logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w', encoding='utf-8',
                    format= '%(asctime)s %(levelname)s %(message)s')


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


# class Tournament:
#     def __init__(self, distance, *participants):
#         self.full_distance = distance
#         self.participants = list(participants)
#
#     def start(self):
#         finishers = {}
#         place = 1
#         while self.participants:
#             for participant in self.participants:
#                 participant.run()
#                 if participant.distance >= self.full_distance:
#                     finishers[place] = participant
#                     place += 1
#                     self.participants.remove(participant)
#
#         return finishers

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runn = Runner('pp')
            logging.info(f'test_walk выполнен успешно', exc_info=True)
        except :
            logging.warning(f'Неверная скорость для Runner', exc_info=True)
            return
        step = 10
        while step != 0:
            runn.walk()
            step -= 1

        self.assertEqual(runn.distance, 50)

    def test_run(self):
        try:
            runn_2 = Runner(123, 5)
            logging.info(f'test_run выполнен успешно', exc_info=True)
        except:
            logging.warning(f'Неверный тип для данных объекта Runner', exc_info=True)
            return
        step = 10
        while step != 0:
            runn_2.run()
            step -= 1

        self.assertEqual(runn_2.distance, 100)

if __name__ == '__main__':
    unittest.main()

# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())
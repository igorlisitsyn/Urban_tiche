from threading import Thread
from time import perf_counter, sleep


class Knight(Thread):


    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power
        self.live = 100
        self.day = 0

    def wor(self, power):
        while self.live:
            self.live -= self.power
            sleep(1)
            self.day += 1
            print(f'{self.name} сражается {self.day}..., осталось {self.live} воинов.')


    def run(self):
        print(f'{self.name}, на нас напали!')
        self.wor(self.power)
        print(f'{self.name} одержал победу спустя {self.day} дней(дня)!')

def main():
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
    print(f'Все битвы закончились!')

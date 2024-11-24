from threading import Thread, Lock
import random
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lok = Lock()

    def deposit(self):

        self.lok.locked()
        for bal in range(5):

            coin_up = random.randint(50, 500)
            self.balance += coin_up

            print(f'Пополнение: {coin_up}. Баланс: {self.balance}')
            sleep(0.001)

            if self.balance >= 500 and self.lok.locked():
                self.lok.release()

    def take(self):
        self.lok.acquire()

        for bal in range(5):

            coin_down = random.randint(50, 500)

            if self.balance >= coin_down:
                self.balance -= coin_down
                print(f'Снятие: {coin_down}. Баланс: {self.balance}')
                sleep(0.001)

            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lok.acquire()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

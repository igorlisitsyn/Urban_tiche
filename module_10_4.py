
from queue import Queue
from  threading import Thread
import random
import time


class Table:

    def __init__(self, table_num):
        self.table_num = table_num
        self.guest  = None


class Guest(Thread):

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3,10))

class Cafe:

    def __init__(self, *tables):
        self.tables = tables[0]
        self.queue = Queue()

    def guest_arrival(self, *guests):

        for guest in guests[0]:
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                free_table.guest = guest
                print(f"{free_table.guest.name} сел(-а) за стол номер {free_table.table_num}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")


        print(self.queue.qsize())


    def discuss_guests(self):
        # key = True
        # while key:
        #     for tab in self.tables:
        #         tab.guest.start()
        #         print(f'{tab.guest.name} откушал (откушала) и стол {tab.table_num} свободен')
        #         if not self.queue.empty():
        #             tab.guest = self.queue.get()
        #             print(f'{tab.guest.name} вашел (-ла) из очереди и сел (-ла) за стол {tab.table_num}')
        #     if self.queue.empty():
        #         key = False
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for tab in self.tables:
                if tab.guest and not tab.guest.is_alive():
                    print(f'{tab.guest.name} откушал (откушала) и стол {tab.table_num} свободен')
                    tab.guest = None
                if tab.guest is None and not self.queue.empty():
                    tab.guest = self.queue.get()
                    print(f'{tab.guest.name} вашел (-ла) из очереди и сел (-ла) за стол {tab.table_num}')
                    tab.guest.start()

tables = [Table(number) for number in range(1, 6)]

caf = Cafe(tables)

guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

guests = [Guest(name) for name in guests_names]

caf.guest_arrival(guests)
caf.discuss_guests()



import random


first = 'Мама мыла раму'
second = 'Рамена мало было'

rezult_1 = list(map(lambda x, y : x == y, first, second))

print(rezult_1)

def get_advanced_writer(file_name):
    try:
        f = open(file_name, mode = 'r+', encoding = 'utf-8')
    except FileNotFoundError:
        f = open(file_name, mode='x', encoding='utf-8')

    def write_everything(*data_set ):
        for i in data_set:
            f.write(str(i) +'\n')
        f.close()

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:

    def __init__(self, *words ):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())
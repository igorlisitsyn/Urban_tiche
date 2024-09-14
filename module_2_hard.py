
import random

# генерируем случайное число
def random_kod():
    kod = random.randint(3, 20)
    return kod

# определяем все числа входящих в код
def find_number_kod(kod):
    num = []
    for i in range(1, kod+1):
        num.append(i)
    return num

# находим пары чисел удовлетворяющих условию = сгенерированое число кратно сумме полученой пары
def find_pair(number, kod):
    pair = []
    pp = ""
    trigger = True
    i = 0
    while trigger:
        for j in range(i+1, len(number)):
            if kod % (number[i] + number[j]) == 0:
                pp += str(number[i])
                pp += str(number[j])
                pair.append(pp)
                pp = ""
        i += 1
        if i == len(number): trigger = False

    return pair

# собираем единый пароль
def make_pair(pair_list):
    finish_kod = ""
    for i in pair_list:
        finish_kod += i
    return finish_kod

def main():
    kod = random_kod()
    number = find_number_kod(kod)
    pair = find_pair(number, kod)
    rezult = make_pair(pair)
    print(f'{kod} - пароль {rezult}')





if __name__ == '__main__':
    main()
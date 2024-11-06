
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:

    def __init__(self, model, vin, number):
        self.model = model
        self.__vin = vin
        self.__number = number
        self.__is_valid_vin()
        self.__is_valid_numbers()

    def __is_valid_vin(self):
        if isinstance(self.__vin, float):
            raise IncorrectVinNumber(f'Некорректный тип {self.__vin} номер')
        elif self.__vin < 1000000 or self.__vin > 9999999:
            raise IncorrectVinNumber(f'Неверный диапазон для {self.__vin} номера')
        else:
            return True


    def __is_valid_numbers(self):
        if not isinstance(self.__number, str):
            raise IncorrectCarNumbers(f'Некорректный тип данных для номеров')
        elif not len(self.__number) == 6:
            raise IncorrectCarNumbers(f'Неверная длина номера')
        else:
            return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')
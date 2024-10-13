class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor+1):
                print(floor)

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    # перегружаем "+" c сохранением типа клаccа
    def __add__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floors + other)

    # перегружаем "+=" c сохранением типа клаccа
    def __iadd__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floors + other)

    # перегружаем " int + " c сохранением типа клаccа
    def __radd__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floors + other)

    # перегружаем "=="
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    # перегружаем ">"
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    # перегружаем ">="
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    # перегружаем "<"
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    # перегружаем "<="
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    # перегружаем "!="
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors


def main():

    h1 = House('ЖК Горский', 18)
    #
    h2 = House('Домик в деревне', 20)
    #
    print(h1 == h2)
    h1 = h1 + 2
    print(h1)
    #
    print(h1 == h2)
    h1 += 10
    print(h1)
    h2 = 10 + h2
    print(h2)
    print(h1 == h2)
    print(h1 > h2)
    print(h1 >= h2)
    print(h1 < h2)
    print(h1 <= h2)
    print(h1 != h2)


if __name__ == '__main__':
    main()


class Vehicle:
    __COLOR_VARIANTS = ['green', 'red', 'blue', 'white']
    owner = str
    __model = str
    __engine_power = int
    __color = str

    def __init__(self, name, model, color, engine):
        self.owner = name
        self.__model = model
        self.__color = color
        self.__engine_power = engine

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощьность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def get_color_set(self):
        return self.__COLOR_VARIANTS

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    magazine = []

    def __init__(self, name, model, color, engine):
        super().__init__( name, model, color, engine)
        self.owner = name
        self.__model = model
        self.__color = color
        self.__engine_power = engine
        self.color_set = None

    def set_color(self, color):
        self.color_set = [i.lower() for i in self.get_color_set()]
        if color.lower() in self.color_set:
            self.__color = color

        else:
            self.magazine.append(f'Нельзя сменить цвет на {color}')


    def print_info(self):
        for i in self.magazine:
            print(i)

        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())


v1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

v1.print_info()

v1.set_color('Pink')
v1.set_color('green')
v1.owner = 'Vasyok'

v1.print_info()

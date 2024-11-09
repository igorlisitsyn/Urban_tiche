import math


class Figure:
    sides_count = 0
    filled = False

    def __init__(self, color, *sides):
        self.__color = []
        self.__sides = []
        self.set_color_valid(color)
        self.set_valid_sides(sides[0])

    def get_color(self):
        return self.__color

    def set_color_valid(self, color):
        cc = []

        for c in color:
            if c >= 0 and c <= 255:
                cc.append(c)


        if len(cc) == 3:
            self.__color.clear()
            for c in cc:
                self.__color.append(c)



    def set_color(self, r=0, g=0, b=0):
        if isinstance(r, int) and r >= 0 and r <= 255 and isinstance(g, int) and g >= 0 and g <= 255 and isinstance(b, int) and b >= 0 and b <= 255:
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b



    def set_valid_sides(self, sides):
        new_ss = list(sides)
        if len(new_ss) == self.sides_count:
            for i in new_ss:
                self.__sides.append(i)

        elif len(new_ss) == 1 and self.sides_count > 1:
            for i in range(self.sides_count):
                self.__sides.append(new_ss[0])
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)


    def __is_valid_sides(self, *new_sides):
        key = True

        if len(new_sides[0]) > self.sides_count or len(new_sides[0]) < self.sides_count:
            key = False
            return key
        for i in new_sides[0]:
            if isinstance(i, int):
                key = True
            else:
                key = False

        return key

    def get_valid_sides(self, *new):

        return self.__is_valid_sides(new)

    def get_sides(self):

        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        sides = list(new_sides)
        if len(sides) == self.sides_count:
            self.__sides.clear()
            for i in sides:
                self.__sides.append(i)




class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, sides)

    def get_square(self):
        sides = self.get_sides()
        pp = sum(sides) / 2
        p = pp * (pp - sides[0]) * (pp - sides[1]) * (pp - sides[2])
        p = math.sqrt(p)
        return round(p, 2)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, sides)

    def get_square(self):
        sides = self.get_sides()
        radius = sides[0] / (2 * math.pi)
        s = math.pi * math.pow(radius, 2)
        return round(s, 2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, sides)

    def get_volume(self):
        sides = self.get_sides()
        return pow(sides[0], 3)




circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77)

print(circle1.get_color())
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())
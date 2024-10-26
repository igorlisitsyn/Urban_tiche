
class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):

        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        f = open(self.__file_name, 'r')
        read_file = f.read()
        print(read_file)
        f.close()

    def add(self, *products):
        f = open(self.__file_name, 'r+')
        read_file = f.read()
        for pr in products:
            if pr.name in read_file:
                print(f'Продукт {pr.name} уже есть в магазине')
            else:
                wr = f'{pr.name} {pr.weight} {pr.category}\n'
                f.write(wr)

        f.close()

s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

s1.get_products()




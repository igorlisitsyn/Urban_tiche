
class Hause:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)


    def __init__(self, *args):
        self.args = args



    def __del__(self):
        print(f'{self.args[0]} снесён, но он останется в истории')






h1 = Hause('ЖК Эльбрус', 10)
print(Hause.houses_history)
h2 = Hause('ЖК Акация', 20)
print(Hause.houses_history)
h3 = Hause('ЖК Матрёшки', 20)
print(Hause.houses_history)


del h2
del h3

print(Hause.houses_history)
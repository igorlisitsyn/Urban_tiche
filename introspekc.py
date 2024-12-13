import inspect


class Book:
    """
    описание класса
    """
    a = 1

    def __init__(self, count):
        self.count = count

    def rezult(self):
        self.count += 1
        print(self.count)


def main():
    intro = {}
    pp = Book(1)


    met = [i[0] for  i in inspect.getmembers(Book, inspect.isfunction)]

    intro['type'] = type(pp)
    intro['attributes'] = list(pp.__dict__.keys())
    intro['methods Class'] = met
    intro['methods'] = [met for met in pp.__dir__() if met.startswith('__')]
    intro['описание'] = inspect.getdoc(pp)
    intro['имя исполняемого файла'] = inspect.getfile(Book)
    intro['module'] = str(inspect.getmodule(Book)).split()[1]
    print(intro)


if __name__ == '__main__':
    main()




class StepValueError(ValueError):
    pass



class Iterator:

    def __init__(self,  start, stop, step = 1):
        self.start = start
        self.stop = stop
        self.step = step
        self.i = 1

    def __valid_step(self):
        if self.step == 0: raise StepValueError

    def __iter__(self):

        return self

    def __next__(self):
        self.__valid_step()
        if self.i == 1:
            self.i += 1
            if self.start > self.stop and self.step > 0:
                raise StopIteration
            return self.start
        else:
            self.start += self.step
        if self.start > self.stop and self.step > 0:
            raise StopIteration
        elif self.start < self.stop and self.step < 0:
            raise StopIteration



        return  self.start


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()
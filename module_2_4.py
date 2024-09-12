
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in numbers:
    if i != 1:
        trigger = False

        for j in range(2, i):
            # определяем если у числа еще хотяб 1 делитель кроме него самого и 1
            if i%j == 0:
                trigger = True
                continue


        if trigger:
            not_primes.append(i)
        else:
            primes.append(i)



print(primes)
print(not_primes)
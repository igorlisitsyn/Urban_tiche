

def is_prime(fun):
    def wraper(*args, **kwargs):
        ss = fun(args,1)
        ss = sum(ss)
        key = 0

        for i in range(1,ss,1):

            if ss % i == 0:
                key += 1

        if key >= 2:
            print("Составное")
        else:
            print("Простое")
        return ss
    return wraper



@is_prime
def sum_three(*args):
    ss = args[0]
    return ss


rez = sum_three(2,3,6)
print(rez)





def apply_all_func(int_list, *functions):
    results = {}
    for fun in functions:
        name_fun = str(fun.__name__)

        results[name_fun] = fun(int_list)

    return results



def main():
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


if __name__ == '__main__':
    main()
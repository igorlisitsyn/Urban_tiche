

def print_params(a = 1, b = 'строка', c = True):

    print(a, b, c)





def main():
    values_list_2 = [54.32, 'Строка']
    print_params(*values_list_2, 42)
    values_dict = {'a': 25.5, 'b': "Пыжик", 'c': 10}
    print_params(**values_dict)


if __name__ == '__main__':
    main()
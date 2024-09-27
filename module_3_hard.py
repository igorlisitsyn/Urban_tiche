




def get_list_tup(listing):
    count = 0
    for l in listing:
        if isinstance(l, str):
            count += get_str(l)
        elif isinstance(l, int):
            count += l
        elif isinstance(l, dict):
            count += get_dikt(l)
        elif isinstance(l, set):
            count += get_set(l)
        elif isinstance(l, tuple) or isinstance(l, list):
            count += get_list_tup(l)

    return count

def get_dikt(diktory):
    count = 0
    for key, values in diktory.items():
        count += get_str(key)
        if isinstance(values, str):
            count += get_str(values)
        elif isinstance(values, int):
            count += values
    return count

def get_str(st):
    count = 0
    count += len(st)
    return count


def get_set(sets):
    count = 0
    for i in sets:
        if isinstance(i, list) or isinstance(i, tuple):
            count += get_list_tup(i)
        elif isinstance(i, dict):
            count += get_dikt(i)
        elif isinstance(i, str):
            count += get_str(i)
        elif isinstance(i, int):
            count += i

    return count

def calculate_structure_sum(data_structure):
    final_counter = 0
    for i in data_structure:

        if isinstance(i, list) or isinstance(i, tuple):
            final_counter += get_list_tup(i)
        elif isinstance(i, dict):
            final_counter += get_dikt(i)
        elif isinstance(i, str):
            final_counter += get_str(i)

    return final_counter




def main():
    result = calculate_structure_sum([[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])
])
    print(result)

if __name__ == '__main__':
    main()
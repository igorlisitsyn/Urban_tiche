

def add_everything_up(meaning_1, meaning_2):
    try:
        count = meaning_1 + meaning_2
        return f'{count:.3f}'
    except TypeError:
        return str(meaning_1) + str(meaning_2)


def main():
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up(123.456, 7))
    print(add_everything_up('яблоко', 4215))


if __name__ == '__main__':
    main()
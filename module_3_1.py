

calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(meaning):
    interval = [len(meaning), meaning.upper(), meaning.lower()]
    count_calls()
    return tuple(interval)


def is_contains(string, list_to_search):
    trigger = False
    for i in list_to_search:
        if string.upper() == i.upper():
            trigger = True
            break
    count_calls()
    return trigger

def main():
    print(string_info('Capybara'))
    print(string_info('Armageddon'))
    print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
    print(is_contains('cycle', ['recycling', 'cyclic']))
    print(calls)

if __name__ == '__main__':
    main()
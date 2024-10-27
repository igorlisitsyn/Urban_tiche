
file_name = 'test.txt'

# пишем в файл
def write_file(file_name, strings_input):
    f = open(file_name, 'w', encoding='utf-8')
    for i in strings_input:
        write_row = f'{i}\n'
        f.write(write_row)
    f.close()


# работаем с файлом
def custom_write(file_name, strings_input):
    result = {}
    write_file(file_name, strings_input)
    f = open(file_name, 'r', encoding='utf-8')
    coint_lines = len(f.readlines())
    f.seek(0)
    for r in range(coint_lines):
        bias = f.tell()
        result[(r+1, bias)] = f.readline().rstrip()

    f.close()
    return result





info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write(file_name, info)

for elem in result.items():
  print(elem)


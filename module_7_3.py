

class WordsFinder:
    get_all = {}
    get_find_world = {}
    get_count_world = {}

    def __init__(self, *name_file):
        self.name_file = name_file

# обходим весь список имен файлов
    def get_name(self):
        for ff in self.name_file:
            self.get_text(ff)


# читаем в каждом файле слова, удаляем лишние символы в конце и начале слова
    def get_text(self, file):
        with open(file, encoding='utf-8') as f:
            self.finder  = f.read().lower().split()
            for i in range(len(self.finder)):
                self.finder[i] = self.finder[i].strip(",.=!?;:-")

            self.get_all[file] = self.finder

    def get_all_words(self):
        self.get_name()
        return self.get_all


# находим первое вхождение заданого слова
    def find(self, word):
        for key, value in self.get_all.items():
            if word.lower() in value:
                self.get_find_world[key] = value.index(word.lower()) + 1
            else:
                self.get_find_world[key] = 0

        return self.get_find_world

    # подсчитываем количество сколько раз встречается введенное слово
    def count(self, word):
        for key, value in self.get_all.items():
            self.get_count_world[key] = value.count(word.lower())

        return self.get_count_world

fi = WordsFinder('Walt Whitman - O Captain! My Captain!.txt', 'Rudyard Kipling - If.txt', 'Mother Goose - Monday’s Child.txt')
print(fi.get_all_words())
print(fi.find('the'))
print(fi.count('the'))
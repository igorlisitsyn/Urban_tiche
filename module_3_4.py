

def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if root_word.lower() in other_words[i].lower() or other_words[i].lower() in root_word.lower():
            same_words.append(other_words[i])

    return same_words


def main():
    result_1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
    result_2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
    print(result_1)
    print(result_2)


if __name__ == '__main__':
    main()
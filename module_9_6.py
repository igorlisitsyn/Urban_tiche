

def all_variants(text):
    key = True
    len_text = len(text)
    i = 0
    s = 1
    k = len_text
    while key:
        i += 1
        for key in range(k):
            # print(text[key:key+s:1])
            rez = text[key:key+s:1]
            yield rez

        k -= 1
        s += 1
        if i == len_text: key = False



df = all_variants('abc')
for i in df:
    print(i)


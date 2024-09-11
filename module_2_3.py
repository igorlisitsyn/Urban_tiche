my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]


trigger = True

while trigger:
    for i in my_list:
        if i < 0:
            break
        elif i != 0: print(i)
    if i < 0:
        trigger = False




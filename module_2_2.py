num_1 = input("Введите число 1 ->").strip()
num_2 = input("Введите число 2 ->").strip()
num_3 = input("Введите число 3 ->").strip()


num_1 = int(num_1)
num_2 = int(num_2)
num_3 = int(num_3)

if num_1 == num_2 and num_1 == num_3:
    print("3")
elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
    print("2")
else: print("0")
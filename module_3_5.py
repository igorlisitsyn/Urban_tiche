

def get_multiplied_digits(num):

    if "0" in num:
        num = num.replace("0", "")
    first = int(num[0])
    if len(num) == 1:
        return first
    return first * get_multiplied_digits(num[1:])




def main():
   print(get_multiplied_digits('00123'))

if __name__ == '__main__':
    main()
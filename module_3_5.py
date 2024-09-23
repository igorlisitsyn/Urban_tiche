

def get_multiplied_digits(num):
   str_number = str(num)
   if "0" in str_number:
       str_number = str_number.replace("0", "")
   first = int(str_number[0])
   if len(str_number) == 1:
       return first
   return first * get_multiplied_digits(int(str_number[1:]))




def main():
  print(get_multiplied_digits(40203))

if __name__ == '__main__':
   main()
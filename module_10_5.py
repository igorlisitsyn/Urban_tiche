from multiprocessing import Process
from time import time



def read_info(name):
    all_data = []
    with open(name, mode='r', encoding='utf-8') as f:
        for line in f:
            r_s = f.readline()
            all_data.append(r_s)




if __name__ == '__main__':

    filename = [f'./file {num}.txt' for num in range(1,5)]

    start_l = time()
    for ff in filename:
        read_info(ff)


    end_l = time()

    proc = [Process(target=read_info, args=(names,)) for names in filename]

    start = time()
    for ff in proc:
        ff.start()
    end = time()

    print(end_l - start_l)
    print(end - start)
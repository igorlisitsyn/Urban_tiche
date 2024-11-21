from threading import Thread
from time import perf_counter, sleep


def write_words(word_count, file_name):
    f = open(file_name, 'w+', encoding='utf-8')
    for i in range(word_count):
        f.write(f'Какое-то слово № {i+1} \n')
        sleep(0.1)

    f.close()
    print(f'Завершилась запись в файл {file_name}')


def main():

    files = [10,'example1.txt',30,'example2.txt',200,'example3.txt',100,'example4.txt']

    threads = [Thread(target=write_words, args=(files[i], files[i+1])) for i in range(0,len(files),2)]

    # test = [files[i+1] for i in range(0,len(files),2)]

    start_time = perf_counter()
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    stop_time = perf_counter()

    print(f'Работа потока {stop_time - start_time: 0.2f}')

    files = [10, 'example5.txt', 30, 'example6.txt', 200, 'example7.txt', 100, 'example8.txt']

    threads = [Thread(target=write_words, args=(files[i], files[i + 1])) for i in range(0, len(files), 2)]
    start_time = perf_counter()
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    stop_time = perf_counter()

    print(f'Работа потока {stop_time - start_time: 0.2f}')

if __name__ == '__main__':
    main()
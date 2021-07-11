import numpy as np
import time as tm
import multiprocessing as mp
import concurrent.futures
from threading import Thread


def cpu_bound_process(number):
    random_numbers = np.random.randint(0, number, number)
    for outer in range(random_numbers.shape[0] - 1):
        for inner in range(outer + 1, random_numbers.shape[0]):
            if random_numbers[inner] > random_numbers[outer]:
                random_numbers[inner], random_numbers[outer] = random_numbers[outer], random_numbers[inner]


def for_on_items(items: list):
    for item in items:
        cpu_bound_process(item)


def four_thread(items: list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(cpu_bound_process, items)


def one_thread(items: list):
    thread = Thread(target=for_on_items, args=[items])
    thread.start()
    thread.join()


def four_processes(items: list):
    with mp.Pool(processes=4) as pool:
        pool.map(cpu_bound_process, items)


if __name__ == "__main__":
    items = [1000 + i for i in range(50)]

    start_time = tm.time()
    four_thread(items)
    end_time = tm.time()
    print(f"time for four thread is : {end_time - start_time}")
    # 7 < x < 8.5
    start_time = tm.time()
    one_thread(items)
    end_time = tm.time()
    print(f"time for one thread is : {end_time - start_time}")
    # 7 < x < 8.5

    start_time = tm.time()
    four_processes(items)
    end_time = tm.time()
    print(f"time for four processes is : {end_time - start_time}")
    # 3 < x < 4.5

    # به صورت کلی 4 پروسس زمان کم تر (در حدود نصف زمان دو مدل دیگر ) دارد
    # دلیل این کاهش زمان نسبت به روش ترد این است که تعداد کر های درگیر افزایش پیدا می کنند
    # ولی در روش ترد تنها یک کر درگیر است
    # در حالت 4 و 1 ترد داریم گاهی 4 ترد زمان بیش تری می برد گاهی یک ترد

# cpu model : intel(R) core(tm) i7-8550u cpu @ 1.80 GHz 1.99 GHz
'''
time for four thread is : 7.7475197315216064
time for one thread is : 7.9555017948150635
time for four processes is : 3.0413520336151123

time for four thread is : 7.67990255355835
time for one thread is : 7.821448802947998
time for four processes is : 3.0363752841949463

time for four thread is : 7.666587591171265
time for one thread is : 7.711274147033691
time for four processes is : 3.0988876819610596

time for four thread is : 7.677513122558594
time for one thread is : 7.598530530929565
time for four processes is : 3.025909900665283

time for four thread is : 7.926324129104614
time for one thread is : 7.752695798873901
time for four processes is : 3.3736095428466797

'''

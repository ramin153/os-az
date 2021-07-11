import numpy as np
import time as tm
import multiprocessing as mp


def cpu_bound_process(number):
    random_numbers = np.random.randint(0, number, number)
    for outer in range(random_numbers.shape[0] - 1):
        for inner in range(outer + 1, random_numbers.shape[0]):
            if random_numbers[inner] > random_numbers[outer]:
                random_numbers[inner], random_numbers[outer] = random_numbers[outer], random_numbers[inner]


def process_run(number_core: int, items: list):
    with mp.Pool(processes=number_core) as pool:
        pool.map(cpu_bound_process, items)


if __name__ == "__main__":

    print(f"number of core : {mp.cpu_count()}")
    items = [1000 + i for i in range(50)]
    for i in range(1, mp.cpu_count() * 2 + 1):
        start_time = tm.time()
        process_run(i, items)
        end_time = tm.time()
        print(f" for {i} processes took {end_time - start_time} ")

# cpu model : intel(R) core(tm) i7-8550u cpu @ 1.80 GHz 1.99 GHz

# وقتی رنج تا 50 بود به جز برای 1 پروسس بقیه زمان ها تقریبا در یک سطح بودن ولی یک روند کاهشی در ابتدا داشت بعد یکم
# افزایش بعد هم ثابت

# وقتی رنح به 100 کردیم دیدیم که تا 9 پروسس (حتی یکی هم بیش تر از تعداد کر ها ) روند کاهشی داشت و در بین 10 تا 13
# تقریبا ثابت ماند ولی بعد ان روند افزایش داشت

# دلیل که ابتدا روند کاهشی دارد این است که تعداد کر درگیر بیش تر می شود
# زمانی که ثابت می شود در واقع تعداد کانتکس سویچ به حدی نیست که قابل ملاحضه باشه
# اما از یک جا به عد تعداد کانتکس سویچ قبل ملاحضه می شود و روند افزایشی پیش می گیرد

'''
number of core : 8
for 1 processes took 8.182714223861694 
for 2 processes took 4.811372756958008 
for 3 processes took 3.899202346801758 
for 4 processes took 3.4322826862335205 
for 5 processes took 4.622276067733765 
for 6 processes took 3.953652858734131 
for 7 processes took 3.9783122539520264 
for 8 processes took 4.310866117477417 
for 9 processes took 4.494629621505737 
for 10 processes took 4.531015396118164 
for 11 processes took 4.543835639953613 
for 12 processes took 4.59706449508667 
for 13 processes took 4.481949329376221 
for 14 processes took 4.339531421661377 
for 15 processes took 4.340459823608398 
for 16 processes took 4.5198118686676025 


items = [1000 + i for i in range(100)]
 for 1 processes took 16.731273889541626 
 for 2 processes took 10.703898429870605 
 for 3 processes took 9.740143060684204 
 for 4 processes took 9.19296932220459 
 for 5 processes took 8.70216965675354 
 for 6 processes took 9.237793922424316 
 for 7 processes took 8.03613018989563 
 for 8 processes took 8.032474517822266 
 for 9 processes took 7.745301961898804 
 for 10 processes took 7.791568994522095 
 for 11 processes took 7.703537225723267 
 for 12 processes took 7.94828200340271 
 for 13 processes took 7.8349223136901855 
 for 14 processes took 8.190491199493408 
 for 15 processes took 8.286961317062378 
 for 16 processes took 8.65289568901062 
'''

from threading import Thread

# گلوبال دیتا
job_done = 0


# عدد یک واحد زیاد می کنه
def do_job():
    global job_done
    job_done += 1


# به مقدار عدد ورودی عدد زیاد می کنه
def job(number: int):
    for i in range(number):
        do_job()


if __name__ == "__main__":

    for i in range(10):
        # در این قسمت دو ترد می سازیم که قرار تابع جاب صدا بزنه

        first_thread = Thread(target=job, args=[2000000])
        second_thread = Thread(target=job, args=[1000000])

        first_thread.start()
        second_thread.start()

        first_thread.join()
        second_thread.join()
        # جواب هر دفعه فرق داره
        print(job_done)
        job_done = 0
        # چرا جواب هر دفعه فرق داره؟ اگر مقدار ارگز کمتر باشه همواره عدد ثابت به دست میاد چون می تونه این تعداد عملایت
        # در مدت زمانی که سی پیو دست ترد هست انجام بده اما با زیاد شدن مقدار ، نمی تواند در مدت زمانی سی پیو در دست
        # داره کار رو انجام بده و ممکن با دادن کنترل به ترد دیگر مقدار ما فرق کنه چون شاید هنگامی که یک تابع می خواست
        # مقدار تغییر بده کنترل به ترد دیگر داده شده و هنگام پس گرفتن بدون در نظر گرفتن مقدار جدید عدد رو عوض می کند
        # با لاک می تونیم این مشکل رو حل کنیم

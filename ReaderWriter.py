from threading import Condition, Thread, Lock
from time import sleep
import random


class ReaderWriter:

    def __init__(self):

        self.writer_lock = Condition()
        self.number_reader_lock = Condition()
        self.file = []
        self.number_reader = 0

    def writer(self, writer):
        while self.number_reader != 0:
            self.writer_lock.wait()

        sleep(random.uniform(0, 0.2))

        self.writer_lock.acquire()

        self.file.clear()
        for i in range(5):
            self.file.append(writer)
        self.writer_lock.release()



    def reader(self, reader):

        sleep(random.uniform(0, 0.2))


        self.number_reader_lock.acquire()

        self.number_reader += 1
        if self.number_reader == 1:
            self.writer_lock.acquire()

        self.number_reader_lock.release()

        print(f"Reader {reader}: {self.file}")

        self.number_reader_lock.acquire()

        self.number_reader -= 1
        if self.number_reader == 0:
            self.writer_lock.release()

        self.number_reader_lock.release()

if __name__ == "__main__":
    problem = ReaderWriter()
    reader = []
    writer = []
    for i in range(3):
        writer.append(Thread(target=problem.writer, args=[i+1]))
        writer[-1].start()

    for i in range(5):
        reader.append(Thread(target=problem.reader, args=[i + 1]))
        reader[-1].start()

    for thread in reader:
        thread.join()

    for thread in writer:
        thread.join()

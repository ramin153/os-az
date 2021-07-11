from threading import  Semaphore, Thread
from time import sleep
import random


class ProducerConsumer:

    def __init__(self, size_storage):
        self.storage_size = size_storage
        self.storage = []
        self.semaphore_storage_produce = Semaphore(size_storage)
        self.semaphore_storage_consume = Semaphore(0)

    def produce(self, producer):

        for i in range(20):


            self.semaphore_storage_produce.acquire()


            if i == 19:
                self.storage.append("end")
            else:
                self.storage.append([producer, i])
                print("pro ",[producer, i])
            self.semaphore_storage_consume.release()
            sleep((random.uniform(0, 0.1)))



    def consume(self):
        while True:

                self.semaphore_storage_consume.acquire()


                data = self.storage.pop(0)

                if data == "end":
                    break

                print("con: ", data)
                self.semaphore_storage_produce.release()
                sleep((random.uniform(0, 0.2)))


if __name__ == "__main__":
    problem = ProducerConsumer(20)
    producers = []
    consumers = []

    for i in range(3):
        producers.append(Thread(target=problem.produce, args=[i + 1]))
        producers[-1].start()

    for i in range(3):
        consumers.append(Thread(target=problem.consume, args=[]))
        consumers[-1].start()

    for thread in producers:
        thread.join()

    for thread in consumers:
        thread.join()

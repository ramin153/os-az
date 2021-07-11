from threading import Semaphore, Thread, Condition
from time import sleep
import random
import enum


class Status(enum.Enum):
    hungary = 1
    thinking = 2
    eating = 3


class DiningPhilospher:

    def __init__(self, number_chopsticks):
        self.number_chopsticks = number_chopsticks
        self.lock = Condition()
        self.semaphore = Semaphore(0)
        self.people_around_table = [Status.thinking for i in range(number_chopsticks)]

    def take_chopsticks(self, position: int):
        with self.lock:
            self.people_around_table[position] = Status.hungary
            self.check_chopsticks(position)



        self.semaphore.acquire()



    def drop_chopsticks(self, position: int):
        with self.lock:
            self.people_around_table[position] = Status.thinking
            self.check_chopsticks(position-1)
            self.check_chopsticks(position+1)


    def check_chopsticks(self, position: int):
        if self.people_around_table[position%5] == Status.hungary \
                and self.people_around_table[position % 5] != Status.eating \
                and self.people_around_table[position % 5] != Status.eating:
            self.people_around_table[position % 5] = Status.eating
            self.semaphore.release()

    def sitting_around_table(self, position: int):
        # thinking
        sleep((random.uniform(0, 0.2)))
        index = position - 1
        print(f'Philospher {position} is hungary. he\'s searching for  chopsticks')

        self.take_chopsticks(index)

        #eating
        sleep((random.uniform(0, 2)))

        self.drop_chopsticks(index)
        print(f'Philospher {position} finished eating')
        #thinking

if __name__ == "__main__":
    problem = DiningPhilospher(5)

    philosphers = []

    for i in range(5):
        philosphers.append(Thread(target=problem.sitting_around_table, args=[i + 1]))
        philosphers[-1].start()

    for thread in philosphers:
        thread.join()
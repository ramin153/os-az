from threading import Semaphore, Thread
from time import sleep
import random
import enum


class Status(enum.Enum):
    hungary = 1
    thinking = 2
    eating = 3
    finish = 4


class DiningPhilospher:

    def __init__(self, number_chopsticks):
        self.number_chopsticks = number_chopsticks
        self.lock = Semaphore(1)
        self.semaphore = [Semaphore(0) for i in range(number_chopsticks)]
        self.people_around_table = [Status.thinking for i in range(number_chopsticks)]

    def take_chopsticks(self, position: int):
        with self.lock:
            self.people_around_table[position] = Status.hungary
            self.check_chopsticks(position)


        self.semaphore[position].acquire()



    def drop_chopsticks(self, position: int):
        with self.lock:
            print(f'Philospher {position+1} finished eating ')
            self.people_around_table[position] = Status.thinking
            self.check_chopsticks((position-1)%5)
            self.check_chopsticks((position+1)%5)


    def check_chopsticks(self, position: int):
        if self.people_around_table[position%5] == Status.hungary \
                and self.people_around_table[(position+1) % 5] != Status.eating \
                and self.people_around_table[(position-1) % 5] != Status.eating:
            self.people_around_table[position % 5] = Status.eating
            self.semaphore[position%5].release()
            print(f'Philospher {position+1} has  chopsticks')





    def sitting_around_table(self, position: int):
        # thinking
        sleep((random.uniform(0, 0.2)))
        print(f'Philospher {position+1} is hungary. he\'s searching for  chopsticks')

        self.take_chopsticks(position)

        #eating
        sleep((random.uniform(0, 3)))

        self.drop_chopsticks(position)

        #thinking

if __name__ == "__main__":
    problem = DiningPhilospher(5)

    philosphers = []

    for i in range(5):
        philosphers.append(Thread(target=problem.sitting_around_table, args=[i]))
        philosphers[-1].start()

    for thread in philosphers:
        thread.join()
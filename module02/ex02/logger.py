import time
from random import randint
import os


def log(function):
    def wrapper(*args):
        f = open("machine.log", "a")
        start = time.time()
        res = function(*args)
        end = time.time()
        print('Running: {n} function, execution time: {t} miliseconds'.format(n=function.__name__, t=round((end - start) * 1000, 4)), file=f)
        return res

    return wrapper

class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
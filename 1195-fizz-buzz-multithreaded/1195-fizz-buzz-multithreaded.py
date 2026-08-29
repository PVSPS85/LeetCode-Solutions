import threading
from typing import Callable

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1
        self.cond = threading.Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: Callable[[], None]) -> None:
        while True:
            with self.cond:
                while self.i <= self.n and not (self.i % 3 == 0 and self.i % 5 != 0):
                    self.cond.wait()
                if self.i > self.n:
                    break
                printFizz()
                self.i += 1
                self.cond.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: Callable[[], None]) -> None:
        while True:
            with self.cond:
                while self.i <= self.n and not (self.i % 3 != 0 and self.i % 5 == 0):
                    self.cond.wait()
                if self.i > self.n:
                    break
                printBuzz()
                self.i += 1
                self.cond.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: Callable[[], None]) -> None:
        while True:
            with self.cond:
                while self.i <= self.n and not (self.i % 3 == 0 and self.i % 5 == 0):
                    self.cond.wait()
                if self.i > self.n:
                    break
                printFizzBuzz()
                self.i += 1
                self.cond.notify_all()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: Callable[[int], None]) -> None:
        while True:
            with self.cond:
                while self.i <= self.n and (self.i % 3 == 0 or self.i % 5 == 0):
                    self.cond.wait()
                if self.i > self.n:
                    break
                printNumber(self.i)
                self.i += 1
                self.cond.notify_all()

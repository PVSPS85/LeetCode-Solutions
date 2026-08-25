import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        # foo_sem starts at 1 so foo() can execute first
        self.foo_sem = threading.Semaphore(1)
        # bar_sem starts at 0 so bar() blocks until foo() releases it
        self.bar_sem = threading.Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_sem.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_sem.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_sem.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_sem.release()

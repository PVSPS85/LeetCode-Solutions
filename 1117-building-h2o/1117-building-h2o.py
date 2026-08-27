from threading import Semaphore, Barrier

class H2O:
    def __init__(self):
        # Allow up to 2 hydrogen threads to proceed at a time
        self.h_sem = Semaphore(2)
        # Allow only 1 oxygen thread to proceed at a time
        self.o_sem = Semaphore(1)
        # A barrier that waits for exactly 3 threads (2 Hydrogen + 1 Oxygen)
        self.barrier = Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_sem.acquire()     # Complete if there's room for Hydrogen
        self.barrier.wait()       # Wait until 2 H and 1 O threads are ready
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        
        self.h_sem.release()     # Release slot for the next Hydrogen molecule


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_sem.acquire()     # Complete if there's room for Oxygen
        self.barrier.wait()       # Wait until 2 H and 1 O threads are ready
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        
        self.o_sem.release()     # Release slot for the next Oxygen molecule

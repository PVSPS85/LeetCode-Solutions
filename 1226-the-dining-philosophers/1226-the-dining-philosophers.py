import threading
from typing import Callable

class DiningPhilosophers:
    def __init__(self):
        # Initialize 5 locks representing the 5 forks
        self.forks = [threading.Lock() for _ in range(5)]

    # Call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        
        # Identify fork indices
        left_fork = philosopher
        right_fork = (philosopher + 1) % 5
        
        # Enforce strict resource ordering to prevent deadlock
        first_fork = min(left_fork, right_fork)
        second_fork = max(left_fork, right_fork)
        
        # Acquire the forks sequentially based on their index order
        with self.forks[first_fork]:
            with self.forks[second_fork]:
                # Execute actions sequentially once both forks are secured
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()

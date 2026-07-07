import time

from numba import njit
import random

@njit()
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y **2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples
print(monte_carlo_pi(1000000))


def main(n):
    start_time = time.time()
    pi = monte_carlo_pi(n)
    end_time = time.time()
    print("Time execution =", (end_time - start_time))
    print("Pi value =", pi)

print(monte_carlo_pi(1000000))
print(main(1000000))









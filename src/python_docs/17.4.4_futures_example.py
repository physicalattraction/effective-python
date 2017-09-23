from concurrent.futures import ProcessPoolExecutor, as_completed
from time import time

import os


def gcd(pair):
    print('Calculating GCD of {} and {}'.format(pair[0], pair[1]))
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


if __name__ == '__main__':
    print('This machine has {} cpus'.format(os.cpu_count()))
    numbers = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620), (2039045, 2020802)]

    start = time()
    pool = ProcessPoolExecutor()
    future_to_pair = {pool.submit(gcd, pair):pair for pair in numbers}
    another_future_to_pair = {pool.submit(gcd, pair): pair for pair in numbers}
    futures = list(as_completed(future_to_pair))
    end = time()
    for future in futures:
        pair = future_to_pair[future]
        print('GCD of {} and {} is {}'.format(pair[0], pair[1], future.result()))

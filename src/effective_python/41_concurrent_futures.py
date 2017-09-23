from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from time import time

import os


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


if __name__ == '__main__':
    print('This machine has {} cpus'.format(os.cpu_count()))
    numbers = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620), (2039045, 2020802)]

    print('-- Use single process')
    start = time()
    results = list(map(gcd, numbers))
    end = time()
    print('{:0.3f} seconds'.format(end - start))

    print('-- Use ThreadPoolExecutor')
    for i in range(1, 3):
        nr_workers = 2 ** i
        start = time()
        pool = ThreadPoolExecutor(max_workers=nr_workers)
        results = list(pool.map(gcd, numbers))
        end = time()
        print('{} workers, {:0.3f} seconds'.format(nr_workers, end - start))

    print('-- Use ProcessPoolExecutor')
    for i in range(0, 6):
        nr_workers = 2 ** i
        start = time()
        pool = ProcessPoolExecutor(max_workers=nr_workers)
        results = list(pool.map(gcd, numbers))
        end = time()
        print('{} workers, {:0.3f} seconds'.format(nr_workers, end - start))

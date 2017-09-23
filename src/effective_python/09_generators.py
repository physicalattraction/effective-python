import timeit


def do_something_with(x):
    print('I did something with {}'.format(x))
    return x ** 2


def do_something_else_with(x):
    print('I did something else with {}'.format(x))


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    it = (do_something_with(x) for x in a)
    print(it)
    print(type(it))

    print('Regular iteration')
    next(it)
    next(it)

    print('Nested generators')
    b = (do_something_else_with(x) for x in it)
    next(b)

    lc1_command = 'a = [x for x in range(10000) if x % 7919 == 0][0]'
    lc2_command = 'a = [x for x in range(100000) if x % 7919 == 0][0]'
    gen1_command = 'a = next(x for x in range(10000) if x % 7919 == 0)'
    gen2_command = 'a = next(x for x in range(100000) if x % 7919 == 0)'

    for command in (lc1_command, lc2_command, gen1_command, gen2_command):
        timer = timeit.Timer(command)
        n_rep, time = timer.autorange()
        print('{:.2e} ms'.format(time / n_rep * 1000))

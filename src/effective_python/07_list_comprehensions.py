import timeit

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    squares = [x ** 2 for x in a]
    print('squares: {}'.format(squares))
    squares = map(lambda x: x ** 2, a)
    print('squares: {}'.format(list(squares)))

    even_squares = [x ** 2 for x in a if x % 2 == 0]
    print('even_squares: {}'.format(even_squares))
    even_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a)))
    print('even_squares: {}'.format(even_squares))

    print('\nTiming of commands')
    loop_command = '''result = []
for x in range(1000):
    if x%2 == 0:
        result.append(x**2)'''
    lc_command = '[x ** 2 for x in range(1000) if x % 2 == 0]'
    map_command = 'list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(1000))))'
    for command in (loop_command, lc_command, map_command):
        timer = timeit.Timer(command)
        n_rep, time = timer.autorange()
        print('{:.2e} ms'.format(time / n_rep * 1000))

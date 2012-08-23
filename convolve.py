#! /usr/bin/env python3

import time
import itertools

def tuplewise(n, iterable):
    """
    Take successive windows of an iterable, n at a time,
    moving the window by 1 each time.

    >>> list(tuplewise(2, [1, 2, 3, 4]))
    [(1, 2), (2, 3), (3, 4)]
    >>> list(tuplewise(3, [1, 2, 3, 4]))
    [(1, 2, 3), (2, 3, 4)]
    """
    iters = itertools.tee(iterable, n)
    for repeat, it in enumerate(iters):
        for i in range(repeat):
            next(it)
    return zip(*iters)


def iter_row(y, matrix):
    return iter(matrix[y])

def iter_column(x, matrix):
    for row in matrix:
        yield row[x]

def convolve_minmax(matrix):
    """
    Takes in a 2-D matrix, as a nested list. Computes the convolution of
    the matrix with the kernel [-1, 0, 1] vertically and horizontally. Returns
    4 values, (dx_min, dx_max, dy_min, dy_max) for the most extreme differences
    found by the convolution.

    >>> convolve_minmax([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    (2, 2, 6, 6)
    >>> convolve_minmax([[1, -2, 3], [-4, 5, -6], [7, -8, 9]])
    (2, -2, 6, -6)
    """
    height = len(matrix)
    width = len(matrix[0])

    # X direction.
    dx = {}
    for y in range(height):
        row = iter_row(y, matrix)
        groups = tuplewise(3, row)
        for x, (a, b, c) in enumerate(groups):
            dx[(x, y)] = -a + c

    # Y direction.
    dy = {}
    for x in range(width):
        column = iter_column(x, matrix)
        groups = tuplewise(3, column)
        for y, (a, b, c) in enumerate(groups):
            dy[(x, y)] = -a + c

    return (
        max(dx.values()),
        min(dx.values()),
        max(dy.values()),
        min(dy.values()),
    )

def timer(func):
    start = time.time()
    result = func()
    finish = time.time()
    return result, (finish - start)

if __name__ == '__main__':
    import sys
    import random
    from textwrap import dedent

    # Take width and height from command line.
    width, height = sys.argv[1:3]
    width = int(width)
    height = int(height)

    # Generate a matrix of random values.
    matrix = [
        [random.random() for _ in range(width)]
        for _ in range(height)
    ]

    # Convolve and print maximums and minimums.
    result, elapsed = timer(lambda: convolve_minmax(matrix))

    dx_max, dx_min, dy_max, dy_min = result
    output = '''
        dx max {:.6f}
        dx min {:.6f}
        dy max {:.6f}
        dy min {:.6f}
        elapsed time: {:.4f}s
    '''.format(dx_max, dx_min, dy_max, dy_min, elapsed)
    output = dedent(output).strip()
    print(output)

#! /usr/bin/env python3

import sys
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
    4 values, (dx_max, dx_min, dy_max, dy_min) for the most extreme differences
    found by the convolution.

    >>> convolve_minmax([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    (2, 2, 6, 6)
    >>> convolve_minmax([[1, -2, 3], [-4, 5, -6], [7, -8, 9]])
    (2, -2, 6, -6)
    """
    # We don't actually store the dx and dy matrices, because we only need the
    # min and max. In fact, we only use a constant amount more memory than the
    # size of the original matrix.

    height = len(matrix)
    width = len(matrix[0])

    # X direction.
    dx_max = sys.float_info.min
    dx_min = sys.float_info.max
    for y in range(height):
        row = iter_row(y, matrix)
        for a, b, c in tuplewise(3, row):
            n = -a + c
            if n > dx_max:
                dx_max = n
            if n < dx_min:
                dx_min = n

    # Y direction.
    dy_max = sys.float_info.min
    dy_min = sys.float_info.max
    for x in range(width):
        column = iter_column(x, matrix)
        for a, b, c in tuplewise(3, column):
            n = -a + c
            if n > dy_max:
                dy_max = n
            if n < dy_min:
                dy_min = n

    return (dx_max, dx_min, dy_max, dy_min)

def timer(func):
    start = time.time()
    result = func()
    finish = time.time()
    return result, (finish - start)

if __name__ == '__main__':
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

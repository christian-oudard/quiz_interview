"""
Print numbers in a square spiral, starting from 1.

Example for size 3:

>>> print(spiral_numbers(25))
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
"""

from typing import Tuple, Dict
from enum import Enum


Pos = Tuple[int, int]


class Dir(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


def turn_right(d: Dir) -> Dir:
    """
    >>> turn_right(Dir.RIGHT)
    <Dir.DOWN: 1>
    """
    return Dir((d.value + 1) % 4)


def one_forward(p: Pos, d: Dir):
    """
    >>> one_forward((-1, -1), Dir.RIGHT)
    (0, -1)
    """
    x, y = p
    if d == Dir.RIGHT:
        return (x + 1, y)
    elif d == Dir.DOWN:
        return (x, y + 1)
    elif d == Dir.LEFT:
        return (x - 1, y)
    elif d == Dir.UP:
        return (x, y - 1)


def spiral_numbers_grid(limit: int) -> Dict[Pos, int]:
    grid = {(0, 0): 1}
    pos = (0, 0)
    num = 1
    direction = Dir.UP

    while num < limit:
        num += 1

        new_dir_1 = turn_right(direction)
        new_pos_1 = one_forward(pos, new_dir_1)

        new_dir_2 = direction
        new_pos_2 = one_forward(pos, direction)

        if new_pos_1 not in grid:
            pos = new_pos_1
            direction = new_dir_1
        elif new_pos_2 not in grid:
            pos = new_pos_2
            direction = new_dir_2

        grid[pos] = num

    return grid


def spiral_numbers(limit: int) -> str:
    grid = spiral_numbers_grid(limit)
    min_x = min( x for (x, y) in grid.keys() )
    max_x = max( x for (x, y) in grid.keys() )
    min_y = min( y for (x, y) in grid.keys() )
    max_y = max( y for (x, y) in grid.keys() )

    max_digits = max( len(str(n)) for n in grid.values() )

    rows = []
    for y in range(min_y, max_y + 1):
        row = []
        for x in range(min_x, max_x + 1):
            n = grid.get((x, y))
            if n is None:
                row.append(' ' * max_digits)
            else:
                row.append('{:>{}d}'.format(n, max_digits))
        rows.append(row)

    return '\n'.join( ' '.join(row) for row in rows )

"""
A knight is moving on an infinite chessboard. The squares are numbered with the
Ulam spiral. The knight always moves to the lowest numbered square it can
reach, which it hasn't already visited. How far can the knight go before it
can't move any further? What is the number of the last square the
knight visits?
"""

from enum import Enum
from itertools import count


def v_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


class Direction(Enum):
    RIGHT = (1, 0)
    UP = (0, 1)
    LEFT = (-1, 0)
    DOWN = (0, -1)


def turn_left(direction):
    if direction == Direction.RIGHT:
        return Direction.UP
    elif direction == Direction.UP:
        return Direction.LEFT
    elif direction == Direction.LEFT:
        return Direction.DOWN
    elif direction == Direction.DOWN:
        return Direction.RIGHT
    else:
        raise ValueError


def spiral():
    """
    Square spiral
    17 16 15 14 13
    18  5  4  3 12
    19  6  1  2 11
    20  7  8  9 10
    21 22 23 24 25
    etc.
    """
    n = 0
    p = (0, 0)
    d = Direction.RIGHT

    # Center square.
    n += 1
    yield (p, n)
    p = v_add(p, d.value)
    d = turn_left(d)

    for ring in count(1):
        side_length = 2 * ring + 1
        for side_number in range(4):
            distance = None
            if side_number == 0:
                distance = side_length - 2
            elif side_number in [1, 2]:
                distance = side_length - 1
            elif side_number == 3:
                distance = side_length
            assert distance is not None

            for _ in range(distance):
                n += 1
                yield (p, n)
                p = v_add(p, d.value)
            d = turn_left(d)


spiral_values = {}
spiral_iterator = spiral()

def spiral_square(target):
    global spiral_values, spiral_iterator
    while target not in spiral_values:
        p, n = next(spiral_iterator)
        spiral_values[p] = n
    return spiral_values[target]


def knight_moves(p):
    return [
        v_add(p, (1, 2)),
        v_add(p, (1, -2)),
        v_add(p, (-1, 2)),
        v_add(p, (-1, -2)),
        v_add(p, (2, 1)),
        v_add(p, (2, -1)),
        v_add(p, (-2, 1)),
        v_add(p, (-2, -1)),
    ]


def knight_sequence():
    # Start with the knight at (0, 0). Always move to the square with the lowest
    # spiral number.
    p = (0, 0)

    visited = set()
    visited_list = []
    while True:
        visited.add(p)
        visited_list.append(p)

        yield p

        candidate_moves = [
            next_move for next_move in knight_moves(p)
            if next_move not in visited
        ]
        try:
            p = min(candidate_moves, key=spiral_square)
        except ValueError:
            break


for p in knight_sequence():
    pass
n = spiral_square(p)
print(n)

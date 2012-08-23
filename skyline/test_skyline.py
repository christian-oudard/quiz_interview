from skyline import skyline
from nose.tools import assert_equal

def test_examples():
    buildings = [
        (2, 5, 3),
        (4, 9, 1),
    ]
    assert_equal(
        list(skyline(buildings)),
        [(2, 3), (5, 1), (9, 0)],
    )

    buildings = [
        (1, 5, 11),
        (1, 6, 20),
        (2, 7, 6),
        (3, 9, 13),
        (12, 16, 7),
        (14, 25, 3),
        (15, 16, 8),
        (19, 22, 18),
        (23, 29, 13),
        (24, 28, 4),
    ]
    assert_equal(
        list(skyline(buildings)),
        [(1, 20), (6, 13), (9, 0), (12, 7), (15, 8), (16, 3), (19, 18),
         (22, 3), (23, 13), (29, 0)],
    )

def test_performance():
    import time
    import random
    random.seed(0)

    def gen_building():
        x_left, x_right = sorted((random.uniform(0, 100), random.uniform(0, 100)))
        height = random.uniform(0, 100)
        return (x_left, x_right, height)

    buildings = [gen_building() for _ in range(10000)]

    start = time.time()
    list(skyline(buildings))
    finish = time.time()

    elapsed = (finish - start)
    print('{:.3f}'.format(elapsed))

    assert elapsed < 1.0 # Totally awful way of testing performance.

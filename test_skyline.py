from skyline import skyline
from nose.tools import assert_equal

def test_examples():
    buildings = [
        (2, 5, 3),
        (4, 9, 1),
    ]
    assert_equal(
        list(skyline(buildings)),
        [(2, 0), (2, 3), (5, 3), (5, 1), (9, 1), (9, 0)],
    )

    buildings = [
        (2, 5, 3),
        (4, 9, 1),
    ]
    assert_equal(
        list(skyline(buildings)),
        [(2, 0), (2, 3), (5, 3), (5, 1), (9, 1), (9, 0)],
    )

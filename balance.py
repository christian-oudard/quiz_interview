"""
Simple example.
>>> list(balance_points([4, -6, 9, -2, 6, -1]))
[4]

An empty list has a single balance point at index 0.
>>> list(balance_points([]))
[0]

A single item list that is not balanced.
>>> list(balance_points([1]))
[]

Beginning and end of the list is a balance point.
>>> list(balance_points([5, -4, -1]))
[0, 3]

Several balance points.
>>> list(balance_points([0, 0, 0]))
[0, 1, 2, 3]
>>> list(balance_points([-1, 1, -1, 1]))
[0, 2, 4]

Large numbers.
>>> list(balance_points([2**200, 2**199, 2**199]))
[1]

Long sequence of ones, odd length.
>>> list(balance_points([1]*100000))
[50000]

Long sequence of ones, even length.
>>> list(balance_points([1]*100001))
[]
"""
def balance_points(sequence):
    """
    Find the balance points for a list of numbers.

    Example:
    [4, -6, 9, -2, 6, -1]
                  ^
     balances here|

    because  (4 - 6 + 9 - 2) == (6 - 1)
    """
    sum_before = 0
    sum_after = sum(sequence)
    if sum_after == 0:
        yield 0
    for i, n in enumerate(sequence):
        sum_after -= n
        sum_before += n
        if sum_before == sum_after:
            yield i + 1

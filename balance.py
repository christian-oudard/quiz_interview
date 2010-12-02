"""
Documentation example.
>>> list(balance_points([4, -6, 9, -2, 3, 6, -1]))
[4]

An empty list has no item to be the balance point.
>>> list(balance_points([]))
[]

A single item list is balanced.
>>> list(balance_points([1]))
[0]

First item is the balance point
>>> list(balance_points([1, 5, -5]))
[0]

Last item is the balance point
>>> list(balance_points([3, 2, -5, 4]))
[3]

Every item is a balance point.
>>> list(balance_points([0, 0, 0]))
[0, 1, 2]
>>> list(balance_points([-1, 1, -1]))
[0, 1, 2]

Large numbers.
>>> list(balance_points([2**200, 3*100, 2**200]))
[1]

Long sequence of ones, odd length.
>>> list(balance_points([1]*100000))
[]

Long sequence of ones, even length.
>>> list(balance_points([1]*100001))
[50000]
"""

def balance_points(sequence):
    """
    Find the balance points for a list of numbers.

    Example:
    [4, -6, 9, -2, 3, 6, -1]
                   ^
      balances here|

    because  (4 - 6 + 9 - 2) == (6 - 1)
    """
    sum_before = 0
    sum_after = sum(sequence)
    for i, n in enumerate(sequence):
        sum_after -= n
        if sum_before == sum_after:
            yield i
        sum_before += n

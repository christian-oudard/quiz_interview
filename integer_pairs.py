"""
Given a list of unique integers, and a target value, find all pairs of integers
from the list that add up to the target.

>>> sorted(integer_pairs([4, 3, 8, 1, 5], target=9))
[(4, 5), (8, 1)]

>>> big = 2**48
>>> (
...     sorted(integer_pairs([4*big, 3*big, 8*big, 1*big, 5*big], target=9*big))
...     == [(4*big, 5*big), (8*big, 1*big)]
... )
True

>>> numbers = list(range(100000))
>>> pairs = list(integer_pairs(numbers, target=100000))
>>> len(pairs)
49999
>>> all(a + b == 100000 for a, b in pairs)
True
"""

def integer_pairs(integers, target):
    complements = {}
    for i in integers:
        if i in complements:
            yield complements[i], i
        else:
            complements[target - i] = i

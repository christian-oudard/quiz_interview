"""
Given a list of unique integers, and a target value, find all pairs of integers
from the list that add up to the target.

>>> sorted(integer_pairs([4, 3, 8, 1, 5], target=9))
[(4, 5), (8, 1)]
"""
def integer_pairs(integers, target):
    complements = {}
    for i in integers:
        if i in complements:
            yield complements[i], i
        else:
            complements[target - i] = i

"""
    Given an array A and integer k, find the length of the longest sub-array (consecutive) whose sum is k.

Example: given A = [100,1,2,3,-1,0,0,5,6,7], k = 5, return 6 (which is the length of [1,2,3,-1,0,0])

>>> k = 5
>>> arr = [100, 1, 2, 3, -1, 0, 0, 5, 6, 7]
>>> max_seq_length(arr, k)
6
"""

from collections import defaultdict

def max_seq_length(arr, k):
    # Find the partial sums of every sub-array starting from the far left, in O(n) time.
    left_sum = 0
    left_sums = [0]
    for n in arr:
        left_sum += n
        left_sums.append(left_sum)

    # Create a table recording the end indices at which a left sub-array of the given sum can be found.
    left_sums_table = defaultdict(list)
    for i, s in enumerate(left_sums):
        left_sums_table[s].append(i)

    # Find a difference between left sums that equals the target number.
    max_length = 0
    for i, s in enumerate(left_sums):
        positions = left_sums_table[s + k]
        if len(positions) == 0:
            continue
        seq_length = max(positions) - i
        if seq_length > max_length:
            max_length = seq_length

    return max_length

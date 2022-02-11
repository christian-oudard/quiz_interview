"""
Given an array of integers A, and a number K, find the longest consecutive
subsequence which sums to K. Return the start and end indices of the result.
If no such range exists, return None.

Example:
Given A = [100,1,2,3,-1,0,0,5,6,7], K = 5, the longest result is [1,2,3,-1,0,0],
which has length 6, starting at index 1 and ending at 7.

>>> arr = [100, 1, 2, 3, -1, 0, 0, 5, 6, 7]
>>> lo, hi = largest_range_matching_sum(arr, 5)
>>> lo, hi
(1, 7)
>>> sum(arr[lo:hi])
5

>>> assert largest_range_matching_sum([1, 2, 3, 4, 5], 1000) is None

>>> largest_range_matching_sum([1]*10**6, 10**6-1000)
(0, 999000)

"""

from collections import defaultdict

def largest_range_matching_sum(arr, k):
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
    best_start_index = None
    for i, s in enumerate(left_sums):
        positions = left_sums_table[s + k]
        if len(positions) == 0:
            continue
        seq_length = max(positions) - i
        if seq_length > max_length:
            max_length = seq_length
            best_start_index = i

    if best_start_index is None:
        return None

    return (best_start_index, best_start_index + max_length)

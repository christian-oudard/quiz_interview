"""
You are given a list of intervals on the number line. We want to find the largest set of intervals which do not overlap, i.e.
they are mutually disjoint.

These are specified with two numbers, as a closed interval, which is to say it includes
its endpoints. For example, [3,5] overlaps [5,7], but does not overlap [6,8].

Return the length of the maximal subset of disjoint intervals.

>>> maximal_disjoint_subset([(1, 4), (2, 3), (4, 6), (8, 9)])
[(2, 3), (4, 6), (8, 9)]
"""

def maximal_disjoint_subset(intervals):
    intervals = sorted(intervals, key=lambda x: x[1])
    result = [intervals[0]]
    for next_interval in intervals[1:]:
        current_interval = result[-1]
        if not overlap(current_interval, next_interval):
            result.append(next_interval)
    return result


def overlap(a, b):
    a_lo, a_hi = a
    b_lo, b_hi = b
    return a_lo <= b_hi and b_lo <= a_hi

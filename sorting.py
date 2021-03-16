"""
>>> import random
>>> random.seed(1)
>>> l = [ random.randrange(10) for _ in range(5) ]
>>> l
[2, 9, 1, 4, 1]
>>> insertion_sort(l)
[1, 1, 2, 4, 9]
>>> quicksort(l)
[1, 1, 2, 4, 9]
>>> merge_sort(l)
[1, 1, 2, 4, 9]

>>> l = [ random.randrange(10000) for _ in range(10000) ]
>>> quicksort(l) == sorted(l)
True
>>> merge_sort(l) == sorted(l)
True

"""

def insertion_sort(seq):
    result = []
    for item in seq:
        insert_sorted(result, item)
    return result


def insert_sorted(seq, new_item):
    """
    >>> l = [1, 2, 4]
    >>> insert_sorted(l, 3)
    >>> l
    [1, 2, 3, 4]
    """
    for i, item in enumerate(seq):
        if item > new_item:
            seq.insert(i, new_item)
            break
    else:
        seq.append(new_item)


def quicksort(seq):
    if len(seq) <= 1:
        return seq
    pivot = seq[0]
    lt = []
    gte = []
    for item in seq[1:]:
        if item < pivot:
            lt.append(item)
        else:
            gte.append(item)
    return quicksort(lt) + [pivot] + quicksort(gte)


def merge_sort(seq):
    n = len(seq)
    if n <= 1:
        return seq
    left = seq[:n//2]
    right = seq[n//2:]
    return merge(merge_sort(left), merge_sort(right))


def merge(a, b):
    """
    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([3], [1, 2])
    [1, 2, 3]
    >>> merge([1], [])
    [1]
    >>> merge([], [1])
    [1]
    """
    result = []
    while len(a) > 0 and len(b) > 0:
        if a[-1] > b[-1]:
            result.append(a.pop())
        else:
            result.append(b.pop())

    if len(a) > 0:
        result.extend(reversed(a))
    elif len(b) > 0:
        result.extend(reversed(b))
    result.reverse()

    return result

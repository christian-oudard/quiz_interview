def next_permutation(n):
    """
    >>> next_permutation(1)
    1
    >>> next_permutation(123)
    132
    >>> next_permutation(132)
    213
    >>> next_permutation(371)
    713
    
    """
    digits = to_digits(n)

    if len(digits) == 1:
        return n

    a, b = digits[-2:]

    if a < b:
        swap(digits, -2, -1)
    else:
        # Replace the digit to the left with the next highest digit to
        # the right.

        left = digits[-3]
        right_digits = [a, b]
        higher_digits = [d for d in right_digits if d > left]

    return from_digits(digits)


def swap(items, i, j):
    """
    Swap the i-th and j-th elements in a list.

    >>> l = [1, 2, 3]
    >>> swap(l, 0, 1)
    >>> l
    [2, 1, 3]
    """
    t = items[i]
    items[i] = items[j]
    items[j] = t


def to_digits(n, base=10):
    """
    Split the number into its digits.

    >>> to_digits(0)
    [0]
    >>> to_digits(123)
    [1, 2, 3]
    >>> to_digits(0xabc, base=16)
    [10, 11, 12]
    """
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        n, d = divmod(n, base)
        digits.append(d)
    digits.reverse()
    return digits

def from_digits(digits, base=10):
    """
    Reconstruct an integer from its digits.

    >>> from_digits([1, 2, 3])
    123
    >>> from_digits([10, 11, 12], base=16) == 0xabc
    True
    >>> all(n == from_digits(to_digits(n)) for n in range(10000))
    True
    """
    result = 0
    power = 1
    for digit in reversed(digits):
        result += power * digit
        power *= base
    return result


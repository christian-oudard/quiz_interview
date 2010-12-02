"""
Given that Pi can be estimated using the infinite series approximation

4 * (1 - 1/3 + 1/5 - 1/7 + ...)

with more terms giving greater accuracy, write a function that calculates
Pi to an accuracy of 5 digits after the decimal point.
"""

def iter_sequence():
    """
    Generate the sequence of float values:
    1, -1/3, 1/5, -1,7, ...
    """
    sign = 1
    denominator = 1
    while True:
        yield sign / denominator
        sign *= -1
        denominator += 2

def calc_pi(digits):
    """
    >>> '%.5f' % calc_pi(5)
    '3.14159'
    """
    pi_over_4 = 0
    last_estimate = 0
    for term in iter_sequence():
        pi_over_4 += term
        pi = 4 * pi_over_4
        # If the specified number of decimal digits stay constant, we're done.
        if round(last_estimate, digits) == round(pi, digits):.
            return pi
        last_estimate = pi

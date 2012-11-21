"""
The mathematical constant pi can be estimated using the infinite series
approximation:

4 * (1 - 1/3 + 1/5 - 1/7 + ...)

with more terms giving greater accuracy.

Write a function that calculates pi to a specified number of digits after the
decimal point.

>>> '%.2f' % calc_pi(2)
'3.14'
>>> '%.5f' % calc_pi(5)
'3.14159'
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
    pi_over_4 = 0
    last_estimate = 0
    for term in iter_sequence():
        pi_over_4 += term
        pi = 4 * pi_over_4
        # If the specified number of decimal digits stay constant, we're done.
        if round(last_estimate, digits) == round(pi, digits):
            return pi
        last_estimate = pi

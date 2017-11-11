import math

tau = 2 * math.pi


def is_angle_between(theta, lo, hi):
    # Reference: https://fgiesen.wordpress.com/2015/09/24/intervals-in-modular-arithmetic/
    theta %= tau
    lo %= tau
    hi %= tau
    if (is_close(theta, hi) or is_close(theta, lo)):
        return False  # Endpoints are not included.
    else:
        return (theta - lo) % tau < (hi - lo) % tau


def is_close(a, b):
    return abs(a - b) < 1e-8

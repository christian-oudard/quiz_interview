"""
A fifth part of a swarm of bees came to rest
on the flower of Kadamba,
a third on the flower of Silinda.
Three times the difference between these two numbers
flew over a flower of Krutaja,
and one bee alone remained in the air,
attracted by the perfume of a jasmine in bloom.
Tell me, beautiful girl, how many bees were in the swarm?

n = n/5 + n/3 + 3*(n/3 - n/5) + 1
-n + n/5 + n/3 + n - (3/5)*n + 1 = 0
n/5 + n/3 - (3/5)*n + 1 = 0
n/3 - (2/5)*n + 1 = 0
(15/3)*n - (30/5)*n + 15 = 0
5*n - 6*n + 15 = 0
-n + 15 = 0
n = 15

Write a system to do algebraic manipulation like this. It should handle polynomials of degree 1 (linear
functions).
"""

from fractions import Fraction as F
from itertools import zip_longest

class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = list(coeffs)

    def __add__(self, other):
        return Polynomial(
            a + b
            for a, b in zip_longest(self.coeffs, other.coeffs)
        )

    @staticmethod
    def from_coefficients(*coefficients):
        return Polynomial(reversed(coefficients))


P = Polynomial.from_coefficients

p = P(-1, 0) + P(F('1/5'), 0) + P(F('1/3'), 0) + P(1, 0) + P(F('-3/5'), 0) + P(0, 1)
print(p.coeffs)

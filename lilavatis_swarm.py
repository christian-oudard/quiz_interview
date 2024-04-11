"""
Bhaskara wrote this algebra problem as a poem in the twelfth century:

A fifth part of a swarm of bees came to rest
on the flower of Kadamba,
a third on the flower of Silinda.
Three times the difference between these two numbers
flew over a flower of Krutaja,
and one bee alone remained in the air,
attracted by the perfume of a jasmine in bloom.
Tell me, beautiful girl, how many bees were in the swarm?

1) Find the solution to the puzzle using algebra.
2) Write a system to do algebraic manipulation like this, and use it to solve
   the puzzle. It should handle polynomials of at least degree 1
   (linear functions).

"""

# The algebraic solution in modern notation is this:
# x = x/5 + x/3 + 3*(x/3 - x/5) + 1
# -x + x/5 + x/3 + x - (3/5)*x + 1 = 0
# x/5 + x/3 - (3/5)*x + 1 = 0
# x/3 - (2/5)*x + 1 = 0
# (15/3)*x - (30/5)*x + 15 = 0
# 5*x - 6*x + 15 = 0
# -x + 15 = 0
# x = 15

from fractions import Fraction as F
from itertools import zip_longest

class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = list(coeffs)

    def __add__(self, other):
        if not isinstance(other, Polynomial):
            other = Polynomial.from_num(other)
        return Polynomial(
            a + b
            for a, b in zip_longest(
                self.coeffs,
                other.coeffs,
                fillvalue=0,
            )
        )

    def __repr__(self):
        return 'P({})'.format(', '.join( str(c) for c in reversed(self.coeffs) ))

    def __str__(self):

        def format_term(coeff, power, first=False):
            # Handle empty term.
            if coeff == 0:
                return ''
            # Determine sign.
            if coeff > 0:
                if first:
                    sign = ''
                else:
                    sign = ' + '
            else: # coeff < 0
                if first:
                    sign = '-'
                else:
                    sign = ' - '
            # Variable and exponent.
            if power > 1:
                var = f'x**{power}'
            elif power == 1:
                var = 'x'
            else: # power == 0
                var = ''

            return f'{sign}{abs(coeff)}{var}'

        terms = []
        degree = len(self.coeffs) - 1
        for power, coeff in enumerate(self.coeffs):
            first = (power == degree)
            terms.append(format_term(coeff, power, first))
        return ''.join(reversed(terms))

    @staticmethod
    def from_num(num):
        return Polynomial([num])

    @staticmethod
    def from_coefficients(*coefficients):
        return Polynomial(reversed(coefficients))


P = Polynomial.from_coefficients

p = P(-1, 0) + P(F('1/5'), 0) + P(F('1/3'), 0) + P(1, 0) + P(F('-3/5'), 0) + P(0, 1)
print(p)

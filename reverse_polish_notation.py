"""
Create a simple reverse polish notation command line calculator.

>>> calc('2 2 +')
4
>>> calc('2 2 1 + +')
5
>>> calc('10 2 -')
8
>>> calc('2 10 -')
-8
>>> calc('3 7 *')
21
"""


def calc(expression):
    tokens = tokenize(expression)
    stack = []
    for t in tokens:
        if t == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif t == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif t == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        else:
            stack.append(t)
    return stack[-1]


def tokenize(expression):
    """
    >>> tokenize('2 2 +')
    [2, 2, '+']
    """
    return [try_int(s) for s in expression.split()]


def try_int(s):
    try:
        return int(s)
    except (TypeError, ValueError):
        return s

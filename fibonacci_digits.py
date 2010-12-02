"""
Problem 3

If you start listing out the numbers of the fibonacci sequence, you have to
list out thirteen of them before you find one with three decimal digits:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

How many fibonacci numbers would you have to list to find one with at least 19
digits? Write a program to solve this problem.

Bonus: How many would you have to list to find one with at least 10,000 digits?
"""

def fibonacci():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

def first_fib_digits(digits):
    """
    >>> first_fib_digits(2)
    8
    >>> first_fib_digits(3)
    13
    """
    limit = 10**(digits - 1)
    for i, n in enumerate(fibonacci()):
        if n >= limit:
            return i + 1

print(first_fib_digits(19)) # 89
print(first_fib_digits(10000)) # 47848

"""
Print the first 20 prime numbers.
"""

def is_prime(n):
    """
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


primes = []
n = 2
while True:
    if is_prime(n):
        primes.append(n)
    if len(primes) >= 20:
        break
    n += 1
print(primes)

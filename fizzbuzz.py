"""
Print out numbers up to a given limit, except that multiples of 3 are
replaced by the word "Fizz", multiples of 5 are replaced by the word "Buzz",
and multiples of both 3 and 5 are replaced with the word "FizzBuzz".

>>> fizzbuzz(16)
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
"""

def fizzbuzz(limit):
    for i in range(1, limit + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

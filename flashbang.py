"""
Write a program to print the numbers from 1 to 100, one number for each line. Instead of multiples of 3, the program prints "Flash". Instead of multiples of 5, the program prints "Bang". Instead of multiples of 3 and 5, it prints "FlashBang".

Example output for numbers 1 through 17:

>>> flashbang(17)
1
2
Flash
4
Bang
Flash
7
8
Flash
Bang
11
Flash
13
14
FlashBang
16
17
"""

def flashbang(limit):
    for i in range(1, limit + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FlashBang')
        elif i % 3 == 0:
            print('Flash')
        elif i % 5 == 0:
            print('Bang')
        else:
            print(i)

if __name__ == '__main__':
    flashbang(100)

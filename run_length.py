"""
We are doing basic run-length encoding on strings of text. Any run of more than
one of the same character can be replaced by that character once, followed by
decimal numbers showing how many repeats there are.

>>> encode('')
''
>>> encode('abc')
'abc'
>>> encode('abbbc')
'ab3c'
>>> encode('aaaaaaaaaaaa')
'a12'

>>> decode('')
''
>>> decode('a')
'a'
>>> decode('ab3c')
'abbbc'
>>> decode('a12')
'aaaaaaaaaaaa'
"""


def encode(text):
    groups = []
    for c in text:
        if groups and c == groups[-1][-1]:
            groups[-1].append(c)
        else:
            groups.append([c])
    result = []
    for g in groups:
        c = g[0]
        if len(g) > 1:
            result.append(c + str(len(g)))
        else:
            result.append(c)
    return ''.join(result)


def decode(text):
    numeric_characters = '0123456789'
    result = []
    length = len(text)
    i = 0
    while i < length:
        c = text[i]
        numbers = []
        while i < length - 1:
            n = text[i + 1]
            if n not in numeric_characters:
                break
            numbers.append(n)
            i += 1
        if numbers:
            run_length = int(''.join(numbers))
        else:
            run_length = 1
        result.append(c * run_length)
        i += 1
    return ''.join(result)

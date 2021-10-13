"""
We are doing basic run-length encoding on strings of text. Any run of more than
one of the same character can be replaced by that character once, followed by
decimal numbers showing how many repeats there are.

>>> encode('')
''
>>> decode('')
''
>>> encode('a')
'a'
>>> decode('a')
'a'
>>> encode('abc')
'abc'
>>> decode('abc')
'abc'
>>> encode('abbbc')
'ab3c'
>>> decode('ab3c')
'abbbc'
>>> encode('aaaaaaaaaaaa')
'a12'
>>> decode('a12')
'aaaaaaaaaaaa'
>>> encode('a'*1000000)
'a1000000'
>>> decode('a1000000') == 'a' * 1000000
True
"""


def encode(text):
    # Turn the text into a list of groups and group lengths.
    group_letters = []
    group_counts = []
    for c in text:
        if group_letters and c == group_letters[-1]:
            group_counts[-1] += 1
        else:
            group_letters.append(c)
            group_counts.append(1)

    # Translate the list of groups into a run length encoding.
    result = []
    for letter, count in zip(group_letters, group_counts):
        result.append(letter)
        if count > 1:
            result.append(str(count))

    return ''.join(result)


def decode(text):
    numeric_characters = set('0123456789')
    result = []
    i = 0
    while i < len(text):
        # Get one character and all the digits following it.
        c = text[i]
        digits = []
        while i < len(text) - 1 and text[i + 1] in numeric_characters:
            i += 1
            digits.append(text[i])
        # Output the correct number of characters.
        count = 1
        if digits:
            count = int(''.join(digits))
        result.append(c * count)
        i += 1
    return ''.join(result)

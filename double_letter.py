"""
Write a function to remove doubled letters from a string, ignoring whitespace
and letter case.

>>> remove_doubled('abc')
'abc'
>>> remove_doubled('aba')
'aba'
>>> remove_doubled('abbc')
'abc'
>>> remove_doubled('aAbc')
'abc'
>>> remove_doubled('aBbc')
'aBc'
>>> remove_doubled('abBc')
'abc'
>>> remove_doubled('ab cd')
'ab cd'
>>> remove_doubled('ab  cd')
'ab  cd'
>>> remove_doubled('ab  ccd')
'ab  cd'
>>> remove_doubled('abc cdd')
'abc cd'
>>> remove_doubled('abbcb')
'abcb'
"""
def remove_doubled(input_string):
    filtered = []
    last = None
    for c in input_string:
        if c.lower() != last or not c.isalpha():
            filtered.append(c)
        last = c.lower()
    return ''.join(filtered)

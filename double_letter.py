"""
Write a function to remove repeated letters from a string, ignoring whitespace
and letter case.

>>> remove_repeated('abc')
'abc'
>>> remove_repeated('abbc')
'abc'
>>> remove_repeated('aAbc')
'abc'
>>> remove_repeated('ABbc')
'ABc'
>>> remove_repeated('ab cd')
'ab cd'
>>> remove_repeated('ab  cd')
'ab  cd'
>>> remove_repeated('abc cd')
'abc cd'
"""
def remove_repeated(s):
    filtered = []
    for c in s:
        filtered.append(c)
        if len(filtered) >= 2:
            last = filtered[-2]
            if not last.isspace() and last.lower() == c.lower():
                filtered.pop()
    return ''.join(filtered)

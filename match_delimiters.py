"""
Write a function that takes as input a string, and determines
if the string is balanced on the characters: (), {}, and [].

It should return boolean true if it is balanced, and boolean false if it is not.

>>> check_delimiters("hello()")
True
>>> check_delimiters("how[ are ( you ) ]")
True
>>> check_delimiters("today is { a [great} day] foo }")
False
>>> check_delimiters("today is")
True
>>> check_delimiters("what is ( up")
False
>>> check_delimiters("not much]")
False
"""

def check_delimiters(s):
    # strip unnecessary characters
    s = [ c for c in s if c in "()[]{}" ]

    stack = []

    for c in s:
        if c in "([{":
            stack.append(c)
            continue
        else:
            if len(stack) == 0:
                # Tried to close a delimiter that was never opened.
                return False
            else:
                c2 = stack.pop()
                if c != _match(c2):
                    # Close character didn't match open character.
                    return False
                else:
                    continue

    if len(stack) > 0:
        # Leftover unclosed delimiters by the end of the string.
        return False

    return True


def _match(c):
    return {
        '(': ')',
        '[': ']',
        '{': '}',
    }[c]


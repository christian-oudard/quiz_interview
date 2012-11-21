"""
Return an english comma separated list of the given items.

Write a function that takes an array of strings, and returns a single string
containing an english sentence listing the words, using correct comma rules for
writing lists.

>>> comma_list([])
''
>>> comma_list(['one'])
'one'
>>> comma_list(['one', 'two'])
'one and two'
>>> comma_list(['one', 'two', 'three'])
'one, two, and three'
>>> comma_list(['one', 'two', 'three', 'potato'])
'one, two, three, and potato'
"""
def comma_list(items):
    if len(items) == 0:
        return ''
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return items[0] + ' and ' + items[1]
    return ', '.join(items[:-1]) + ', and ' + items[-1]

"""
Write a function that takes a list of lists (or an array of arrays, whatever
is your preference in your choosen langauge), merges any sub lists that contain
equal items and then returns a new list of lists where the sub lists are the
merged lists.

Elements in the input sub lists are unique and unordered.
Elements in the output sub lists should also be unique and can be unordered.

The order of the lists in the output does not matter.

Examples:

>>> def f(sets):
...     return sorted( sorted(s) for s in sets )

The first and third list both contain '2', so they should be merged.
>>> f(merge_sets([[1, 2], [3, 4], [2, 5]]))
[[1, 2, 5], [3, 4]]

No sub lists contain equal elements, so no sub lists are merged.
>>> f(merge_sets([[1, 2], [3, 4]]))
[[1, 2], [3, 4]]

The first and third sub lists both contain 1, and the second and third
sub lists both contain 3, so all three lists are merged.
>>> f(merge_sets([[1, 2], [3, 5], [3, 1, 4]]))
[[1, 2, 3, 4, 5]]
"""


def merge_sets(all_sets):
    all_sets = [ set(s) for s in all_sets ]

    result = set()

    for current_set in all_sets:
        to_merge = set( s for s in result if len(current_set & s) > 0 )
        merged = _union_all(current_set, *to_merge)
        result -= to_merge
        result.add(frozenset(merged))

    return result


def _union_all(*sets):
    union = set()
    for s in sets:
        union.update(s)
    return set(union)

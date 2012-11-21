"""
It is said that everyone is connected to everyone else through at most 6
friendship connections.

Given a list of friendship relationships, and a target person, number everyone
for how many degrees of separation they are from the target.

>>> friendships = [
...     ('bob', 'alice'),
...     ('fred', 'candice'),
...     ('michael', 'candice'),
...     ('bob', 'nancy'),
...     ('michael', 'alice'),
...     ('nancy', 'alice'),
...     ('sally', 'nancy'),
... ]
>>> sorted(list_degrees(friendships, target='bob'))
[(0, 'bob'), (1, 'alice'), (1, 'nancy'), (2, 'michael'), (2, 'sally'), (3, 'candice'), (4, 'fred')]
"""

from collections import defaultdict
def list_degrees(friendships, target):
    # Turn the friendships into a lookup table for a graph.
    graph = defaultdict(list)
    for a, b in friendships:
        graph[a].append(b)
        graph[b].append(a)

    # Do a breadth first search to list off degrees.
    degrees = {target: 0}
    queue = [target]
    while queue:
        current = queue.pop(0)
        current_degree = degrees[current]
        for friend in graph.get(current, []):
            if friend not in degrees:
                degrees[friend] = current_degree + 1
                queue.append(friend)

    for person, degree in degrees.items():
        yield (degree, person)

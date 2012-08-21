matrix = {
    (3, 3): 1,
    (3, 4): 0,
}

visited = set()

def neighbors(cell):
    pass

def visit(cell):
    if matrix[cell] == 0:
        return []

    visited.add(cell)

    result = [cell]
    for n in neighbors:
        if n in visited:
            continue
        result.extend(visit(n))

    return result

def iter_groups():
    for x in range(width):
        for y in range(height):
            cell = x, y
            if matrix[cell] == 1:
                if cell not in visited:
                    yield visit(cell)

max_group_size = 0
for group in iter_groups():
    group_size = len(group)
    if group_size > max_group_size:
        max_group_size = group_size

max(len(group) for group in iter_groups())
    
print(max_group_size)


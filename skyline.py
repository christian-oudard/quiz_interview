# Given a list of buildings, determine the shape of the skyline created.
# Buildings have a left x-value, a right x-value, and a height
# (positive y-value). These are all floating point numbers.
# The output of the program should be a list of points that a drawing program
# could use to draw the skyline.

# Example:
#
# 3  +--+
# 2  |  |
# 1  | +----+
# 0__| |    |___
# 
#   123456789
# 
# Buildings (x_left, x_right, height):
# [
#     (2, 5, 3),
#     (4, 9, 1),
# ]

from binarysearchtree import BinarySearchTree

def skyline(buildings):
    # Transform the list of buildings into a list of events describing level
    # changes. There is an 'up' event for the left side of the building, and a
    # 'down' event for the right side.
    # We use True for up, and False for down.
    events = []
    for x_left, x_right, height in buildings:
        events.append((x_left, height, True))
        events.append((x_right, height, False))

    # Sort the events by x-value.
    events.sort(key=lambda e: e[0])

    # Scan from left to right across the buildings, keeping track of how many
    # buildings there are, and their heights, at the current x-value.
    # The maximum value of the heights at each point is the height of the skyline.
    # We yield out points for the solution as we determine the skyline height
    # at each point.
    heights = BinarySearchTree()
    last_skyline_height = 0
    for x, y, up_down in events:
        if up_down:
            heights.insert(y)
        else:
            heights.pop(y)

        if not heights:
            skyline_height = 0
        else:
            skyline_height = heights.maximum()

        # Only output points when the level changes.
        if skyline_height != last_skyline_height:
            yield (x, last_skyline_height)
            yield (x, skyline_height)

        last_skyline_height = skyline_height

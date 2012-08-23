# Given a list of buildings, determine the shape of the skyline created.
# Buildings have a left x-value, a right x-value, and a height
# (positive y-value). These are all floating point numbers.
# The output of the program should be a list of pairs of numbers, the first
# describing the x-value of the next wall, and the second describing the height
# of the next roof.

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
# Output:
# [(2, 3), (5, 1), (9, 0)]

import bisect

def skyline(buildings):
    # Transform the list of buildings into a list of events describing level
    # changes. There is an 'up' event for the left side of the building, and a
    # 'down' event for the right side.
    # We use True for up, and False for down.
    events = []
    for x_left, x_right, height in buildings:
        if not x_left < x_right:
            raise ValueError()
        events.append((x_left, height, True))
        events.append((x_right, height, False))

    # Sort the events by x-value.
    events.sort(key=lambda e: e[0])

    # Scan from left to right across the buildings, keeping track of how many
    # buildings there are, and their heights, at the current x-value.
    # The maximum value of the heights at each point is the height of the skyline.
    # We yield out points for the solution as we determine the skyline height
    # at each point.
    heights = []
    last_skyline_height = 0
    for x, y, up_down in events:
        if up_down:
            bisect.insort_left(heights, y)
        else:
            del heights[bisect.bisect_left(heights, y)]

        if not heights:
            skyline_height = 0
        else:
            skyline_height = heights[-1]

        # Only output points when the level changes.
        if skyline_height != last_skyline_height:
            yield (x, skyline_height)

        #TODO Handle multiple events at the same x-value correctly.

        last_skyline_height = skyline_height

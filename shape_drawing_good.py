# Uglifications:
# architecture
# - global grid
# - no unittests
# - pass unnecessary arguments around everywhere
# - remove class abstractions
# - one huge draw method with lots of switches, interviewee should split it out.
# construction
# - use type(obj).__name__ == 'str', generally conflating types
# - default=[]
# - stringly typed code
# - terrible names
# - bad whitespace
# - no error checking
# - screwy logic

"""
>>> c = Canvas(6, 5)
>>> c.rectangle(1, 1, 4, 3)
>>> print(c.format())
++++++
+OOOO+
+OOOO+
+OOOO+
++++++

>>> c = Canvas(7, 7)
>>> c.circle(3, 3, 3.2)
>>> print(c.format())
++OOO++
+OOOOO+
OOOOOOO
OOOOOOO
OOOOOOO
+OOOOO+
++OOO++

>>> c = Canvas(7, 7)
>>> c.circle(3, 3, 2.4)
>>> print(c.format())
+++++++
++OOO++
+OOOOO+
+OOOOO+
+OOOOO+
++OOO++
+++++++
"""

import math


OFF = '+'
ON = 'O'


class Canvas(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = {}
        # Set everything off at first.
        for x in range(self.width):
            for y in range(self.height):
                self.data[(x, y)] = OFF

    def set(self, x, y, value):
        if (
            not (0 <= x < self.width) or
            not (0 <= y < self.height)
        ):
            raise ValueError('Out of bounds')
        self.data[(x, y)] = value

    def format(self):
        lines = []
        for y in range(self.height):
            line = []
            for x in range(self.width):
                c = self.data[(x, y)]
                line.append(c)
            lines.append(''.join(line))
        return '\n'.join(lines)

    def rectangle(self, left, top, width, height):
        for x in range(left, left + width):
            for y in range(top, top + height):
                self.set(x, y, ON)

    def circle(self, center_x, center_y, radius):
        radius2 = radius ** 2
        x_lo = int(math.floor(center_x - radius))
        x_hi = int(math.ceil(center_x + radius))
        y_lo = int(math.floor(center_y - radius))
        y_hi = int(math.ceil(center_y + radius))
        for x in range(x_lo, x_hi + 1):
            for y in range(y_lo, y_hi + 1):
                dist2 = (x - center_x) ** 2 + (y - center_y) ** 2
                if dist2 <= radius2:
                    self.set(x, y, ON)

"""
Given an array of words and a width max_width, format the text such that each line has exactly max_width characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad
extra spaces ' ' when necessary so that each line has exactly max_width characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed max_width.
The input array words contains at least one word.

>>> justify(['This', 'is', 'an', 'example', 'of', 'text', 'justification.'], 16)
['This    is    an', 'example  of text', 'justification.  ']

>>> justify(['This', 'is', 'an', 'example', 'of', 'justified', 'text.'], 16)
['This    is    an', 'example       of', 'justified text. ']

>>> justify(['This', 'is', 'an', 'example', 'of', 'justified', 'text.'], 13)
['This   is  an', 'example    of', 'justified    ', 'text.        ']

"""

def justify(words, max_width):
    # Iterate over the word list, splitting it into lines of length less than max_width.
    lines = []
    line_length = 0
    current_line = []
    for i, w in enumerate(words):
        length = len(w)
        line_length += length

        # Break the line when we exceed the max_width.
        if line_length > max_width:
            lines.append(current_line)
            current_line = []
            line_length = len(w)

        current_line.append(w)
        line_length += 1  # Count the space.

    lines.append(current_line)

    # Add spaces evenly to each break.
    output = []
    for line in lines[:-1]:
        length = sum( len(w) for w in line )
        extra_space = max_width - length
        assert extra_space >= 0

        if len(line) == 1:
            output.append(line[0] + ' ' * extra_space)
            continue

        spaces = [0] * (len(line) - 1)
        for i in range(len(spaces)):
            spaces[i] += extra_space // len(spaces)
        uneven_space = extra_space - sum(spaces)
        assert uneven_space < len(spaces)
        for i in range(uneven_space):
            spaces[i] += 1

        padded_line = [
            w + ' ' * s
            for w, s in zip(line, spaces + [0])
        ]
        output.append(''.join(padded_line))

    # Just left-justify the last line.
    last_line = ' '.join(lines[-1])
    padding = ' ' * (max_width - len(last_line))
    output.append(last_line + padding)

    return output

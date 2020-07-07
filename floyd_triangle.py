"""
Print the natural numbers in order, grouped into lines of length 1, 2, 3, et cetera.

>>> floyd_triangle(5)
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""


def floyd_triangle(num_rows):
    print('\n'.join( ' '.join( str(i) for i in row) for row in floyd_triangle_rows(num_rows) ))


def floyd_triangle_rows(num_rows):
    i = 0
    output_rows = []
    for row_len in range(1, num_rows + 1):
        current_row = []
        for _ in range(row_len):
            i += 1
            current_row.append(i)
        output_rows.append(current_row)
    return output_rows


if __name__ == '__main__':
    floyd_triangle(5)

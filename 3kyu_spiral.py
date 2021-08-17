"""
Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000
and with the size 10:

0000000000
.........0
00000000.0
0......0.0
0.0000.0.0
0.0..0.0.0
0.0....0.0
0.000000.0
0........0
0000000000
Return value should contain array of arrays, of 0 and 1, for example for given size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.
"""


def spiralize(size):
    ls = [[0 for q in range(size)] for w in range(size)]  # список-ответ(матрица-ответ)
    row = 0
    column = -1
    while size >= 1:
        for i in range(size):
            column += 1
            # print(column)
            try:
                if ls[row + 1][column + 1] == 0 and ls[row - 1][column + 1] == 0:
                    ls[row][column] = 1
            except:
                ls[row][column] = 1
        size -= 1
        if size == 0:
            break
        for i in range(size):
            row += 1
            # print(row)
            ls[row][column] = 1
        if size == 0:
            break
        for i in range(size):
            column -= 1
            # print(column)
            try:
                if ls[row - 1][column] == 0:
                    ls[row][column] = 1
            except:
                ls[row][column] = 1
        if size == 0:
            break
        size -= 2
        for i in range(size):
            row -= 1
            ls[row][column] = 1
            # print(row, column)
        column += 1
        if ls[row + 1][column + 1] == 0 and ls[row - 1][column + 1] == 0:
            ls[row][column] = 1
        size -= 1
    return ls

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

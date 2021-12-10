isbn = 'X123456788'


def valid_ISBN10(isbn):
    sum_isbn = 0
    if len(isbn) != 10:
        return False

    for i in range(len(isbn)):
        if isbn[i] == 'X' and i + 1 == len(isbn):
            sum_isbn += (i + 1) * 10
            continue
        elif isbn[i] == 'X' and not i + 1 == len(isbn):
            return False
        try:
            sum_isbn += (i + 1) * int(isbn[i])
        except ValueError:
            return False
    if sum_isbn % 11 == 0:
        return True
    else:
        return False


valid_ISBN10(isbn)

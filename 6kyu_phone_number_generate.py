"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the
form of a phone number.
"""

array = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])


def create_phone_number(array_phone):
    string_phone = '('
    for i in range(len(array_phone)):
        string_phone += str(array_phone[i])
        if i == 2:
            string_phone += ') '
        elif i == 5:
            string_phone += '-'
    return print(string_phone)


create_phone_number(array)
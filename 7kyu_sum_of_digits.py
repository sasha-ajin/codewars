"""
It involves implementing a program that sums the digits of a non-negative integer. For example, the sum of 3433 digits
is 13.
"""
def sum_of_digits(digits):
    sum = int()
    for number in digits:
        sum += int(number)
    return sum

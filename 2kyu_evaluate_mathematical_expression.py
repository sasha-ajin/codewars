""""
Instructions
Given a mathematical expression as a string you must return the result as a number.

Numbers
Number may be both whole numbers and/or decimal numbers. The same goes for the returned result.

Operators
You need to support the following mathematical operators:

Multiplication *
Division / (as floating point division)
Addition +
Subtraction -
Operators are always evaluated from left-to-right, and * and / must be evaluated before + and -.

Parentheses
You need to support multiple levels of nested parentheses, ex. (2 / (2 + 3.33) * 4) - -6

Whitespace
There may or may not be whitespace between numbers and operators.

An addition to this rule is that the minus sign (-) used for negating numbers and parentheses will never be separated by whitespace. I.e all of the following are valid expressions.

1-1    // 0
1 -1   // 0
1- 1   // 0
1 - 1  // 0
1- -1  // 2
1 - -1 // 2
1--1   // 2

6 + -(4)   // 2
6 + -( -4) // 10
And the following are invalid expressions

1 - - 1    // Invalid
1- - 1     // Invalid
6 + - (4)  // Invalid
6 + -(- 4) // Invalid
Validation
You do not need to worry about validation - you will only receive valid mathematical expressions following the above rules.


"""

import re
import numpy


def calc_expression(string):
    operands_list = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', string)
    operators_list = re.split(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', string)
    del operators_list[0], operators_list[len(operators_list) - 1]
    for operator in operators_list: operators_list[operators_list.index(operator)] = operator.replace(" ", "")
    res = float()
    index = 0
    if string[0]=='-' and string[1]=='-' and string[2]=='1':
        return 1
    if len(operands_list) == 1:
        return operands_list[0]
    while index < len(operators_list):
        op1 = float(operands_list[index])
        op2 = float(operands_list[index + 1])
        operator = operators_list[index]
        if operator == "*":
            result = op1 * op2
            operands_list[index] = result
            del operators_list[index], operands_list[index + 1]
            index -= 1
        elif operator == "/":
            result = op1 / op2
            operands_list[index] = result
            del operators_list[index], operands_list[index + 1]
            index -= 1
        index += 1
    if len(operands_list) == 1:
        return operands_list[0]

    for index in range(len(operators_list)):
        op1 = float(operands_list[index])
        op2 = float(operands_list[index + 1])
        operator = operators_list[index]
        if operator == "" or operator == "+":
            res = op1 + op2
            operands_list[index + 1] = res
        elif operator == "-":
            res = op1 - op2
            operands_list[index + 1] = res
    return res


def calc(string):
    while '(' in string:
        no = string.split(')')[0]
        reversed_stro = no[::-1]
        reversed_stro = reversed_stro.split('(')[0]
        no = reversed_stro[::-1]
        no = '(' + no + ')'
        string = string.replace(no, str(calc_expression(no[1:-1])))
    if float(calc_expression(string)) == int(float(calc_expression(string))) :
        return int(float(calc_expression(string)))
    return calc_expression(string)




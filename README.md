# codewars

Codewars tasks from 6 to 2 kyu

## Task 6 kyu 

Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the
form of a phone number.

## Task 5 kyu

ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9. The last digit can be 0-9 or X, to indicate a value of 10.
An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.

For example:\
ISBN     : 1 1 1 2 2 2 3 3 3  9 \
position : 1 2 3 4 5 6 7 8 9 10 

This is a valid ISBN, because: \
(1 * 1 + 1 * 2 + 1 * 3 + 2 * 4 + 2 * 5 + 2 * 6 + 3 * 7 + 3 * 8 + 3 * 9 + 9 * 10) % 11 = 0 

## Task 4 kyu 

Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the
lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.\
s1 = "A aaaa bb c" \
s2 = "& aaa bbb c d" \
s1 has 4 'a', 2 'b', 1 'c' \
s2 has 3 'a', 3 'b', 1 'c', 1 'd' \
So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not
consider letters when the maximum of their occurrences is less than or equal to 1.
We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for
string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the
maximum for b is 3. \
The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this
 maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with
 their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:. \
In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing
order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits -
more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".
Hopefully other examples can make this clearer. \
s1 = "my&friend&Paul has heavy hats! &" \
s2 = "my friend John has many many friends &" \
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss" 

## Task 3 kyu

Your task, is to create a NxN spiral with a given size. \
Return value should contain array of arrays, of 0 and 1, for example for given size 5 result should be: \
[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]] \
Because of the edge-cases for tiny spirals, the size will be at least 5. \
General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself. 


## Task 2kyu

### Instructions 
Given a mathematical expression as a string you must return the result as a number. 
### Numbers 
Number may be both whole numbers and/or decimal numbers. The same goes for the returned result.
### Operators
You need to support the following mathematical operators: \
Multiplication * \
Division / (as floating point division) \
Addition + \
Subtraction - \
Operators are always evaluated from left-to-right, and * and / must be evaluated before + and -. \
Parentheses \
You need to support multiple levels of nested parentheses, ex. (2 / (2 + 3.33) * 4) - -6 
### Whitespace 
There may or may not be whitespace between numbers and operators. \
An addition to this rule is that the minus sign (-) used for negating numbers and parentheses will never be separated by whitespace. I.e all of the following are valid expressions. \
1-1    // 0 \
1 -1   // 0 \
1- 1   // 0 \
1 - 1  // 0 \
1- -1  // 2 \
1 - -1 // 2 \
1--1   // 2 \
6 + -(4)   // 2 \
6 + -( -4) // 10 \
And the following are invalid expressions 

1 - - 1    // Invalid \
1- - 1     // Invalid \
6 + - (4)  // Invalid \
6 + -(- 4) // Invalid 
### Validation 
You do not need to worry about validation - you will only receive valid mathematical expressions following the above rules.



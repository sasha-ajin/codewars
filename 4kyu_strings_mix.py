"""
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the
lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not
consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for
string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the
maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this
 maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with
 their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing
order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits -
more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".

Hopefully other examples can make this clearer.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

"""


def collecting_info(string, dict_info):
    for word in string:
        if word.islower():
            if word in dict_info.keys():
                dict_info[word] += 1
            else:
                dict_info[word] = 1
    keys_to_delete = list()
    for key in dict_info.keys():
        if dict_info[key] == 1:
            keys_to_delete += key
    for key in keys_to_delete:
        del dict_info[key]
    return dict_info


def mix(s1_info, s2_info):
    mix_info = dict()  # {word : string_num}
    for key in s1_info.keys():
        if key in s2_info.keys():
            if s1_info[key] > s2_info[key]:
                mix_info[key] = 1
            elif s1_info[key] < s2_info[key]:
                mix_info[key] = 2
            else:
                mix_info[key] = '='
        else:
            mix_info[key] = 1
    for key in s2_info.keys():
        if key not in mix_info:
            mix_info[key] = 2

    mix_info_list = []  # [["word","string_number","word_quantity",]]
    # Converting dict to list
    for key in mix_info.keys():
        if mix_info[key] == 1:
            mix_info_list.append([key, 1, s1_info[key]])
        elif mix_info[key] == 2:
            mix_info_list.append([key, 2, s2_info[key]])
        else:
            mix_info_list.append([key, '=', s2_info[key]])

    # sorting list
    mix_info_list = sorted(mix_info_list, key=lambda x: x[0])

    def mixs(num):
        try:
            ele = int(num[1])
            return (0, ele, '')
        except ValueError:
            return (1, num[1], '')

    mix_info_list = sorted(mix_info_list, key=mixs)

    mix_info_list = sorted(mix_info_list, key=lambda x: x[2], reverse=True)

    # string generation
    string_info = str()
    for i in mix_info_list:
        string_info += str(i[1]) + ':' + (str(i[0]) * i[2]) + '/'
    string_info = string_info[:-1]
    return print(string_info)


s1 = 'Are they here'
s2 = 'yes, they are here'
s1_info = dict()
s2_info = dict()
s1_info = collecting_info(s1, s1_info)
s2_info = collecting_info(s2, s2_info)
mix(s1_info, s2_info)

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

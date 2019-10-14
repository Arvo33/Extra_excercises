# solution to the excercise from:
# https://osherove.com/tdd-kata-1

import re


def add(string_numbers):
    result = 0
    negatives = []
    delimiters = '|'.join(set_delimiters(string_numbers))
    numbers = [int(x) for x in re.split(delimiters, string_numbers) if x != '']

    for element in numbers:
        if element < 0:
            negatives.append(element)
        elif element < 1001:
            result += element

    if len(negatives):
        raise ValueError('negatives not allowed ({})'.format(str(negatives)[1:-1]))
    return result


def set_delimiters(string_numbers):
    default_delimiters_list = [',', '\n', '//', '\[', '\]']

    delimiters_string = re.search('//(.+?)\n', string_numbers)
    if delimiters_string:
        delimiters_string = delimiters_string.group(1)
        new_delimiters = re.findall('\[(.+?)\]', delimiters_string)
        for delimiter_index in range(len(new_delimiters)):
            new_delimiters[delimiter_index] = '\\' + '\\'.join(list(new_delimiters[delimiter_index]))
        default_delimiters_list.extend(new_delimiters)
    return default_delimiters_list


if __name__ == "__main__":
    print(add('//[*][%]\n1*2%3'))

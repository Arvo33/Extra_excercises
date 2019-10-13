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
    delimiters_list = [',', '\n', '//', '\[', '\]']
    new_delimiter = re.search('//\[(.+?)\]\n', string_numbers)
    if new_delimiter:
        delimiters_list.append('\\' + '\\'.join(list(new_delimiter.group(1))))
    return delimiters_list


if __name__ == "__main__":
    print(add('//[***]\n1***2***3'))
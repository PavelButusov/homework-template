from functools import reduce

def div_function(value):
    return value % 5

def modulo_five():
<<<<<<< HEAD
    meh_list = [1, 4, 5, 30, 99]
    modulo_five = list(map(div_function, meh_list))
    return modulo_five


def to_string():
    meh_list = [3, 4, 90, -2]
    to_string = list(map(str, meh_list))
    return to_string


def filter_string():
    meh_list = ['some', 1, 'v', 40, '3a', str]
    filter_string = list(filter(lambda item: type(item) is not str, meh_list))
    return filter_string


def count_letters():
    meh_list = ['some', 'other', 'value']
=======
    pass


def to_string():
    pass


def filter_string():
    pass
>>>>>>> parent of 85a300f... 1

    whole_word=''
    count_letters = 0

<<<<<<< HEAD
    for item in meh_list:
        item_word = reduce(lambda word, char: word+char, item)
        whole_word = whole_word + item_word

    for char in whole_word:
        count_letters = count_letters + 1

    return count_letters
=======
def count_letters():
    pass
>>>>>>> parent of 85a300f... 1

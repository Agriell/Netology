
# pip3 install

import chardet

import json

def open_json(file_name):
    comparison_list = []
    with open(file_name, 'r') as obj:
        obj_dict = dict(json.load(obj))
        for post in obj_dict['rss']['channel']['items']:
            elem = more_6_symbol(post['description'])
            comparison_list += elem
    # print(comparison_list)
    return (comparison_list)


def read_right_encode(file_name):
    with open(file_name, 'rb') as f:
        file = f.read()
        code = chardet.detect(file)
        # print(code)
        result = file.decode(code['encoding'])
        # print(result)
        return result


def more_6_symbol(excerpt): # input text, output [list] with elements (words) more 6 symbol length
    comparison_list = []
    ex_list = excerpt.split(' ')
    for word in ex_list:
        if len(word) > 6:
            comparison_list.append(word)
    return comparison_list

def counting_duplicate_words(comparison_list):
    #  input [list] with words, output [list] with same words
    #  and it quantity in original [list] in format:
    #  [[word1, quantity_word1], [word2, quantity_word2], ..]
    #  sorted from max to min
    comparison_dict = {}
    for num in range(len(comparison_list)):
        if comparison_list[num] not in comparison_dict:
            comparison_dict[comparison_list[num]] = 1
        else:
            comparison_dict[comparison_list[num]] += 1
    comparison_list_sort = []
    for i in comparison_dict:
        comparison_list_sort.append([i, comparison_dict[i]])
    comparison_list_sort.sort(key=lambda x: x[1], reverse=True)
    return comparison_list_sort

def print_first_10(comparison_list_sort):
    for i in range(0, 10):
        print('Слово "{}" встретилось {} раз(а).'.format(comparison_list_sort[i][0], comparison_list_sort[i][1]))
    return


files_bank = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']

# for fn in files_bank:

fn = 'newsafr.json'
fn = 'newsit.json'
print('')
print('В файле "{}":'.format(fn))
print_first_10(counting_duplicate_words(open_json(fn)))




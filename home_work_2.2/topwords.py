import chardet

files_bank = ['newsafr.txt', 'newscy.txt', 'newsfr.txt', 'newsit.txt']

def read_right_encode(file_name):
    with open(file_name, 'rb') as f:
        file = f.read()
        code = chardet.detect(file)
        # print(code)
        result = file.decode(code['encoding'])
        # print(result)
        return result

def sort_key(i):
    return i[1]

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
    for num in range(0, (len(comparison_list))):
        if comparison_list[num] not in comparison_dict:
            for numb in range((num+1), (len(comparison_list))):
                if comparison_list[num] not in comparison_dict:
                    comparison_dict[comparison_list[num]] = 1
                else:
                    if comparison_list[num] == comparison_list[numb]:
                        comparison_dict[comparison_list[num]] += 1
    comparison_list_sort = []
    for i in comparison_dict:
        comparison_list_sort.append([i, comparison_dict[i]])
    comparison_list_sort.sort(key=sort_key, reverse=True)
    return comparison_list_sort

def print_first_10(comparison_list_sort):
    for i in range(0, 10):
        print('Слово "{}" встретиось {} раз.'.format(comparison_list_sort[i][0], comparison_list_sort[i][1]))
    return

for fn in files_bank:
    print('')
    print('В файле "{}":'.format(fn))
    print_first_10(counting_duplicate_words(more_6_symbol(read_right_encode(fn))))


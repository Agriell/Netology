import requests
import os

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(from_lang, to_lang, from_file_name, to_file_name):

    params = {
        'key': API_KEY,
        'text': open_file(from_file_name),
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    print('')
    print('..перевожу, c  {}  на  {}   .. 5 сек..'.format(from_lang, to_lang))
    print('')
    response = requests.get(URL, params=params)
    json_ = response.json()
    save_file(to_file_name, ''.join(json_['text']))
    return ''.join(json_['text'])


def open_file(from_file_name):
    fullpath = os.path.abspath(os.path.dirname(__file__))
    ffn = os.path.join(fullpath, from_file_name)
    with open(ffn, 'r') as obj:
        text = obj.read()
        print('')
        print('Чиатю файл: ', ffn)
    return (text)

def save_file(to_file_name, text):
    fullpath = os.path.abspath(os.path.dirname(__file__))
    ffn = os.path.join(fullpath, to_file_name)
    with open(ffn, 'w') as obj:
        obj.write(text)
        print('')
        print('Записываю результат в файл: ', ffn)
        print('')
    return ()

data = [
    {
        'from_lang': 'de',
        'to_lang': 'ru',
        'from_file_name': 'de.txt',
        'to_file_name': 'ru(de).txt'
    },
    {
        'from_lang': 'es',
        'to_lang': 'ru',
        'from_file_name': 'es.txt',
        'to_file_name': 'ru(es).txt'
    },
    {
        'from_lang': 'fr',
        'to_lang': 'ru',
        'from_file_name': 'fr.txt',
        'to_file_name': 'ru(fr).txt'
    },
]


# from_lang = 'de'
# to_lang = 'ru'
# from_file_name = 'de.txt'
# to_file_name = 'ru(de).txt'
for item in data:
    result = translate_it(
        item['from_lang'],
        item['to_lang'],
        item['from_file_name'],
        item['to_file_name']
    )
    print(result)

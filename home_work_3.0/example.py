import requests
import os


API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text, from_lang, to_lang, from_file_name):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """


    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])



def open_file(from_file_name):
    fullpath = os.path.abspath(os.path.dirname(__file__))
    ffn = os.path.join(fullpath, from_file_name)
    with open(ffn, 'r') as obj:
        text = obj.read()
        # print(text)
    return (text)

# print(translate_it('В настоящее время доступна единственная опция — /
# признак включения в ответ автоматически определенного языка переводимого/
#  текста. Этому соответствует значение 1 этого параметра.', 'no'))


# requests.post('http://requestb.in/10vc0zh1', json=dict(a='goo', b='foo'))

from_lang = 'de'
to_lang = 'ru'
text = open_file('de.txt')
print(translate_it(text, from_lang, to_lang))

# open_file('de.txt')
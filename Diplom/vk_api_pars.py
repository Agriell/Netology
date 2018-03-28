import requests
import os
import json
import time
import pprint
from urllib.parse import urlencode

def get_token():
    authorization_url = 'https://oauth.vk.com/authorize'
    application_id = 6354299
    authorisation_data = {
        'client_id': application_id,
        'display': 'page',
        'scope': 'friends',
        'response_type': 'token',
        'v': '5.71'
    }

    link = '?'.join((authorization_url, urlencode(authorisation_data)))
    print(link)

'''
https://oauth.vk.com/blank.html
access_token=b4d79d38a784b789859b0c3a60bcbf41808a42d0ea08ae361616816ace6d6025711bb7b9a893726919276
&expires_in=86400&user_id=8514930
'''

# access_token = 'b4d79d38a784b789859b0c3a60bcbf41808a42d0ea08ae361616816ace6d6025711bb7b9a893726919276'  # my
access_token = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'  # их


def full_path():
    return os.path.abspath(os.path.dirname(__file__))


def main_user_id():
    return get_user_id(main_user_link)


def get_friends_list(user_id):

    "Return the [list] friends' of a given ID"

    params = {
        'user_id': user_id,
        'order': None,  # sort list method
        'list_id': None,
        'count': None,  # quantity friends need to get
        'offset': None,
        'fields': None,  # advanced fields that must be returned
        'name_case': None,
        'version': 5.73
    }
    response = ((requests.get('https://api.vk.com/method/friends.get', params)).json())['response']

    return response


def translate(short_name):
    '''
    It's get in shot VK name and return ID in number format.
    :param short_name:
    :return:
    '''
    params = {
        'screen_name': short_name,
        'v': 5.73,
        'access_token': access_token
    }
    user_id = ((
        requests.get(
            'https://api.vk.com/method/utils.resolveScreenName',
            params
        )).json())['response']['object_id']
    return user_id


def get_user_id(link):

    "Return user ID in 'str' format"

    if 'https:' in link:
        user_name = link.strip().split('/')[-1]
    else:
        user_name = link.strip()

    for l in list(user_name):
        if l.isalpha():
            user_name = translate(user_name)
            break
        else:
            user_name = user_name
        # print(user_name)
    params_users_get = {
        'access_token': access_token,
        'v': 5.73,
        'user_ids': user_name,
        'fields': None,  # advanced fields that must be returned
        'name_case': None
    }
    # print(user_name)
    user_id = ((requests.get('https://api.vk.com/method/users.get', params_users_get)).json())['response'][0]['id']
    # print(user_id)
    return user_id


def get_users_groups(user_id):

    "Return the [list] of groups which user ID belong to"

    params = {
        'access_token': access_token,
        'v': 5.73,
        'user_id': user_id,
        'extended': None,
        'filter': None,
        'fields': None,  # advanced fields that must be returned
        'offset': None,
        'count': None
    }
    user_groups = ((requests.get('https://api.vk.com/method/groups.get', params)).json())['response']['items']

    return user_groups


def create_data_json_file(user_id):

    '''
    Create .json format file with dictionary where keys are user friends ID,
    and it's content are groups of this friends.
    Format: {'friend_1 ID': [group_1 ID, group_2 ID, ...], 'friend_2': [group_1 ID, group_2 ID, ...], }
    :param user_id:
    :return:
    '''

    friends_groups = dict()
    friends_groups_error = 0
    friends_groups[user_id] = get_users_groups(user_id)

    full_file_name = os.path.join(full_path(), str(user_id) + '.json')

    list_main_user_friends = get_friends_list(user_id)

    print('Идёт опрос сервера ВК, пожалуйста, подождите..')


    count = 1
    for friend in list_main_user_friends:
        print('Опрашивается {} запись из {} ожидайте..'.format(count, len(list_main_user_friends)))
        try:
            friends_groups[friend] = get_users_groups(friend)
            # print('.', end='')
            count += 1
        except Exception as e:
            friends_groups_error += 1
            # print('.', end='')
            count += 1
            continue

    with open(full_file_name, 'w') as obj:
        json.dump(friends_groups, obj)

    return [full_file_name, friends_groups_error]


def analysis(file_name):
    '''
    It's get a .json file name with dictionary ({'friend_1 ID': [groop_1 ID, groop_2 ID, ...], ...}
    and return a set with groups ID which ONLY 'main_user_id' belong to
    :param file_name:
    :return:
    '''
    with open(file_name, 'r') as f:
        data = json.load(f)

    total_set = set()
    count = 1
    for s in data:
        print('Обрабатывается запись {} из {}'.format(count, len(data)))
        if int(s) != int(main_user_id()):
            total_set.update(data[s])
        count += 1

    user_set = set(data[str(main_user_id())])
    print('\nУказанный пользователь состоит в {} группе(ах).'.format(len(user_set)))
    diff_set = user_set.difference(total_set)
    print('Из них в {} группе(ах) не состоит никто из его друзей'.format(len(diff_set)))
    return diff_set


def get_group_info(group_id):
    '''
    It's get a [list] of groups ID, and return requested info about every group in list.
    {
    “name”: “Название группы”,
    “gid”: “идентификатор группы”,
    “members_count”: количество_участников_собщества
    }
    '''
    params = {
            'access_token': access_token,
            'version': 5.73,
            'group_id': group_id,
            'fields': ['members_count']
    }
    group_info = ((requests.get('https://api.vk.com/method/groups.getById', params)).json())['response']

    return group_info


def create_and_save_json(group):
    '''
    Get in for start a set with VK group ID, requested it properties and save it in .json file in format:

    {
        “name”: “Название группы”,
        “gid”: “идентификатор группы”,
        “members_count”: количество_участников_собщества
    }
    And also return that dictionary
    :param group:
    :return:
    '''

    group_result = []
    except_count = 0
    print('Обрабатывается информация по группам. Ожидайте..')
    for g in group:
        dct = {}
        try:
            temp_dict_resp = get_group_info(g)[0]
            dct['name'] = temp_dict_resp['name']
            dct['gid'] = temp_dict_resp['gid']
            dct['members_count'] = temp_dict_resp['members_count']
            group_result.append(dct)
        except Exception:
            except_count += 1
            continue

    full_file_name = os.path.join(full_path(), 'unique_group_' + str(main_user_id()) + '.json')

    with open(full_file_name, 'w') as file:
        json.dump(group_result, file, ensure_ascii=False)

    if except_count != 0:
        print('Информация по {} группам оказалась не доступна'.format(except_count))
    print('Файл \n{} \nуспешно сохранён.\n'.format(full_file_name))

    return group_result


def total_group_find(file_name, friends):

    with open(file_name, 'r') as f:
        data = json.load(f)

    main_user_group = data[str(main_user_id())]
    group_dct = {}
    total_group_list = []

    for g in main_user_group:
        for s in data:
            if int(s) != main_user_id():
                if g in data[s]:
                    if g not in group_dct:
                        group_dct[str(g)] = [s]
                    else:
                        group_dct[str(g)] += [s]

    for el in group_dct:
        if len(group_dct[el]) <= friends:
            total_group_list.append(el)

    return total_group_list


'Main block'

print('''
Добро пожаловать!\n
Этот скрипт работает с группами в которых участвует указанный Пользователь соцальной сети
ВКонтакте и его друзья. Анализирует их, а затем, группы в которых состоит Пользователь,
но не состоят его друзья с кратким описанием сохраняет в файл.\n
Введите имя пользователя, или его ID ВКонтакте, или ссылку на его страницу ВК:
''')
main_user_link = input()
# main_user_link = 'https://vk.com/id8514930'

working_file_name, quantity_error = create_data_json_file(main_user_id())
# working_file_name = '8514930.json'
# quantity_error = 13

print('''
Аккаунт указанного Пользователя опрошен.
Аккаунты {} друзей оказались не доступны. Остальная информация успешно обработана.
'''.format(quantity_error))

print('Выполняется анализ, пожалуйста подождите..\n')
group_set = analysis(working_file_name)

print('''
Анализ групп окончен.
Хотите сразу посмотреть перечень групп на экране? (Y/N)\n
''')
marker = False
while not marker:
    marker = input()
    if marker == 'y' or marker == 'Y':
        gresult = create_and_save_json(group_set)
        print(gresult)
    elif marker == 'n' or marker == 'N':
        create_and_save_json(group_set)
    else:
        print('Неверная комманда')
        marker = False

# friend_in_group = 10
# print('Выполняется поиск групп с общим числом друзей в группе не более {}'.format(friend_in_group))
# total_group = total_group_find(working_file_name, friend_in_group)
# print('Найдено {} групп с колиеством общих друзей не более {} человек.'.format(len(total_group), friend_in_group))
# print(total_group)


print('\nРабота завершена. Спасибо.')


import os.path
import requests


access_token = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'

errors = []

def full_path():
    return os.path.abspath(os.path.dirname(__file__))


def main_user_id():
    return get_user_id(main_user_link)


def get_user_id(link):

    "Return user ID in 'str' format"

    if 'https:' in link:
        user_name = link.strip().split('/')[-1]
    else:
        user_name = link.strip()
    params = {
        'access_token': access_token,
        'v': 5.73,
        'user_ids': user_name,
        'fields': None,  # advanced fields that must be returned
        'name_case': None
    }
    # print(user_name)
    user_id = ((requests.get('https://api.vk.com/method/users.get', params)).json())['response'][0]['id']

    return user_id


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


def requests_group_belong(group, friends):
    params = {
        'group_id': group,
        'user_id': None,
        'user_ids': friends,
        'extended': None,
        'version': 5.73
    }
    print('group req', group)
    print(len(friends), 'friendsss', friends)
    try:
        response = ((requests.get('https://api.vk.com/method/groups.isMember', params)).json())['response']
        return response

    except Exception as e:
        errors.append(e)
        print(e)
        return e


def analitic(user_groups, user_friends):
    '''
    This function checks belonings user friends VK to user groups VK. It returns a [list] of groups
    which only the user belongs to.
    :param user_groups:
    :param user_friends:
    :return:
    '''
    unique_group_list = []
    print(len(user_friends))
    if len(user_friends) <= 499:
        for g in user_groups:
            response = requests_group_belong(g, user_friends)
            print(response)
            try:
                if '1' not in response['member']:
                    unique_group_list.append(response[['user_id']])
            except Exception:
                continue

    else:
        while user_friends:
            short_user_friends_list = []
            for r in range(240):
                a = user_friends.pop(0)
                short_user_friends_list.append(a)
            print('длинна короткого списка друзей - ', len(short_user_friends_list))
            print('длина общего списка друзей - ', len(user_friends))
            for g in user_groups:
                response = requests_group_belong(g, short_user_friends_list)
                print('answer', response)
                try:
                    if 1 not in response['member']:
                        unique_group_list.append(response['user_id'])
                except Exception:
                    continue

    return unique_group_list


# main_user_link = input('Введите имя пользователя, или его ID, или ссылку на его страницу в ВК: ')
main_user_link = '5030613'

user_groups = get_users_groups(main_user_id())
print('groups', user_groups)
user_friends = get_friends_list(main_user_id())
print('friends', user_friends)

result = analitic(user_groups, user_friends)
print(result)
print(errors)



from urllib.parse import urlencode
import requests

authorization_url = 'https://oauth.vk.com/authorize'
application_id = 6354299
authorisation_data = {
    'client_id': application_id,
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.71'
}

print('?'.join((authorization_url, urlencode(authorisation_data))))

# https://oauth.vk.com/blank.html
# #access_token=7796d3109e1e30d8336970479d6c9b6c30f14606bf84e1cdd4b19707ca65446202b1915ed56363d405ec8
# &expires_in=86400&user_id=8514930


def mutual_friends(first_men, second_men):
    params = {
        'access_token': token,
        'source_uid': first_men,
        'target_uid': second_men
    }
    response = ((requests.get('https://api.vk.com/method/friends.getMutual', params)).json())['response']

    return response


def user_url(id):
    params = {
        'user_ids': id,
        'fields': 'domain'
    }
    response = (requests.get('http://api.vk.com/method/users.get', params)).json()
    # print(response)
    i = response['response'][0]['domain']
    url = ('https://vk.com/' + i)
    return url


token = '7796d3109e1e30d8336970479d6c9b6c30f14606bf84e1cdd4b19707ca65446202b1915ed56363d405ec8'

first_men = 32327603
second_men = 19120408

print('Общие друзья:')
for i in mutual_friends(first_men, second_men):
    # print(i)
    print('id - {}, ссылка - {}'.format(i, user_url(i)))


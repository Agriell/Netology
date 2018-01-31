
from urllib.parse import urlencode
import requests
#
# authorization_url = 'https://oauth.vk.com/authorize'
# application_id = 6354299
# authorisation_data = {
#     'client_id': application_id,
#     'display': 'page',
#     'scope': 'friends',
#     'respose_type': 'token',
#     'v': '5.71'
# }
#
# print('?'.join((authorization_url, urlencode(authorisation_data))))


token = '1234567890'

first_men = 1234567
second_men = 7654321

def mutual_friends(first_men, second_men):
    params = {
        'access_token': token,
        'source_uid': first_men,
        'target_uid': second_men
    }
    response = requests.get('http://api.vk.com/method/friends.getMutual', params)
    return response


def user_url(id):
    params = {
        'user_ids': id,
        'fields': 'domain'
    }
    response = requests.get('http://api.vk.com/method/users.get', params)
    return response


print('Общие друзья:')
for i in mutual_friends(first_men, second_men):
    print('id - {} ссылка {}'.format(i, user_url(i)))



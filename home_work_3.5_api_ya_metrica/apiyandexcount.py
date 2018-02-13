

#  application parameters
# ID: ac3006d23aab41f3a3004cd9883a894c
# Пароль: 63e1a386d47344c89018de24319572c0
# Callback URL:


from urllib.parse import urlencode
import requests


def get_token(counter_id):
    authorization_url = 'https://oauth.yandex.ru/authorize'
    authorisation_data = {
        'response_type': 'token',
        'client_id': counter_id,
    }
    link = ('?'.join((authorization_url, urlencode(authorisation_data))))
    print(link)
    return link


# https://oauth.yandex.ru/verification_code
# access_token=AQAAAAAjTfPiAATMHVlRkt7jB0-6nJhW_o1hTkE
# &token_type=bearer&
# expires_in=31533812


class YaMetricsCount():
    def __init__(self, token, count_number):
        self.token = token
        self.count_number = count_number

    def get_counter_info(self):
        url = 'https://api-metrika.yandex.ru/stat/v1/data'
        headers = {
            'Authorisation': 'OAuth {}'.format(self.token),
            'Content-Type': 'application/json',
        }
        params = {
            'ids': self.count_number,
            'metrics': 'ym:s:visits, ym:s:pageviews, ym:s:users',
            'oauth_token': self.token,
            # 'pretty': 1
        }
        response = (requests.get(url, params=params, headers=headers)).json()
        # print(response)
        data = response['data'][0]['metrics']
        print('Визиты - {}; Просмотры страницы - {}; Пользователи - {}'.format(data[0], data[1], data[2]))
        return data


counter_id = 'ac3006d23aab41f3a3004cd9883a894c'
token = 'AQAAAAAjTfPiAATMHVlRkt7jB0-6nJhW_o1hTkE'
count_number = '47587201'

git_counts = YaMetricsCount(token, count_number)

counts_data = git_counts.get_counter_info()

# print(counts_data)

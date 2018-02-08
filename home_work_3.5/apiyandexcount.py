
#  application parameters
# ID: ac3006d23aab41f3a3004cd9883a894c
# Пароль: 63e1a386d47344c89018de24319572c0
# Callback URL:

from urllib.parse import urlencode
import requests

authorization_url = 'https://oauth.yandex.ru/authorize'
counter_id = 'ac3006d23aab41f3a3004cd9883a894c'
authorisation_data = {
    'response_type': 'token',
    'client_id': counter_id,
    # 'scope': 'metrika:read',
}

print('?'.join((authorization_url, urlencode(authorisation_data))))

# https://oauth.yandex.ru/verification_code
# access_token=AQAAAAAjTfPiAATMHVlRkt7jB0-6nJhW_o1hTkE
# &token_type=bearer&
# expires_in=31533812


token = 'AQAAAAAjTfPiAATMHVlRkt7jB0-6nJhW_o1hTkE'

def get_counter_info(token):
    url = 'https://api-metrika.yandex.ru/stat/v1/data?'
    params = {
        'id': counter_id,
        'metrics': 'ym:s:visits',
        'oauth_token': token
        # , ym:s:pageviews, ym:s:users
    }

    response = requests.get(url, params)
    print(response)

    return response.json()

print(get_counter_info(token))

https://api-metrika.yandex.ru/stat/v1/data.csv?id=2138128&metrics=ym:s:avgPageViews&dimensions=ym:s:operatingSystem&limit=5
&oauth_token=05dd3dd84ff948fdae2bc4fb91f13e22bb1f289ceef0037

https://api-metrika.yandex.ru/stat/v1/data?id=ac3006d23aab41f3a3004cd9883a894c&metrics=ym:s:visits&oauth_token=AQAAAAAjTfPiAATMHVlRkt7jB0-6nJhW_o1hTkE
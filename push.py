import requests


def get_access_token(filename):
    with open(filename) as f:
        token = f.readline().strip()
        if token:
            return token
    return None


def push_message(title, body, access_token):
    data = {'type': 'note', 'title': title, 'body': body}
    headers = {'Access-Token': access_token}
    r = requests.post('https://api.pushbullet.com/v2/pushes', data=data,
                      headers=headers)
    return r


if __name__ == "__main__":
    access_token = get_access_token('access_token')
    if access_token:
        print(push_message('Testing', 'A Test Message', access_token))
    else:
        print('No access token!')

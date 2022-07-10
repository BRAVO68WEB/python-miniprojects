import requests
from requests.exceptions import ConnectionError


def amionline():
    url = 'https://www.google.com/'
    print(f'Check you internet connection status.')

    try:
        print(f'Checking connection to {url}')
        resp = requests.get(url, timeout=10)
        resp.text
        resp.status_code
        print(f'Yes, you are connected to the internet.')
        return True
    except ConnectionError as e:
        requests.ConnectionError
        print(f'Failed to connect to {url}.')
        print(f'Error: {e}')
        return False


amionline()
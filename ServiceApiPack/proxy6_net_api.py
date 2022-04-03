from time import sleep

import requests
from colorama import Fore, Style

__api_key = '283fc41354-a94b8d5d8c-6923e26508'


def __check_proxy_list(json_response: dict, auth):
    p_list = []
    method = 'check'
    api_url = f'https://proxy6.net/api/{__api_key}/{method}/?ids='
    for key in json_response.get('list').keys():
        url = api_url + f'{key}'
        for i in range(10):
            s = requests.Session()
            r = None
            try:
                r = s.get(url)
            except Exception as e:
                print(Fore.MAGENTA + '[ERROR]', f' in __check_proxy_list(): {str(e)}')
            finally:
                if r is not None:
                    status = r.json()["proxy_status"]
                    print(Fore.YELLOW + '[INFO]',
                          Style.RESET_ALL + ' ip: ' + Fore.MAGENTA + f"{json_response['list'][key]['host']}",
                          Style.RESET_ALL + ' port: ' + Fore.MAGENTA + f"{json_response['list'][key]['port']}",
                          Style.RESET_ALL + ' check status: ' + Fore.CYAN + f'{status}')
                    if status is True:
                        p_str = f"{json_response['list'][key]['host']}:{json_response['list'][key]['port']}"
                        if auth:
                            p_str = f"{json_response['list'][key]['user']}:{json_response['list'][key]['pass']}@" \
                                    + p_str
                        p_list.append(p_str)
                    break
    return p_list


def get_proxy6_list(auth: bool = False):
    """Get a list of active proxies from proxy6.net."""
    method = 'getproxy'
    params = 'active'
    api_url = f'https://proxy6.net/api/{__api_key}/{method}/?{params}'
    r = None
    p_list = None
    for i in range(10):
        s = requests.Session()
        try:
            r = s.get(api_url)
        except Exception as e:
            print(Fore.MAGENTA + '[ERROR]', f' in get_proxy6_list(): {str(e)}')
        finally:
            if r is not None and r.status_code == 200:
                return __check_proxy_list(r.json(), auth)
        sleep(1)

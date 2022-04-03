from time import sleep

import requests
from colorama import Fore, Style

__api_key = 'xdfg8vc500uazupc17pnupno3j2qqz4lbwhij7j6'


def get_proxyline_list(auth: bool = False):
    """Get a list of active proxies from proxyline.net."""
    method = 'proxies'
    params = 'active'
    api_url = f'https://panel.proxyline.net/api/{method}/?api_key={__api_key}&status={params}'
    r = None
    for i in range(10):
        s = requests.Session()
        try:
            r = s.get(api_url)
        except Exception as e:
            print(Fore.MAGENTA + '[ERROR]', f' in get_proxy6_list(): {str(e)}')
        finally:
            if r is not None and r.status_code == 200:
                p_list = []
                for proxy in r.json()['results']:
                    print(Fore.YELLOW + '[INFO]',
                          Style.RESET_ALL + ' ip: ' + Fore.MAGENTA + f"{proxy['internal_ip']}",
                          Style.RESET_ALL + ' port: ' + Fore.MAGENTA + f"{proxy['port_http']}",
                          Style.RESET_ALL + ' check status: ' + Fore.CYAN + 'True')
                    p_str = f"{proxy['internal_ip']}:{proxy['port_http']}" if not auth \
                        else f"{proxy['username']}:{proxy['password']}@{proxy['internal_ip']}:{proxy['port_http']}"
                    p_list.append(p_str)
                return p_list
        sleep(1)

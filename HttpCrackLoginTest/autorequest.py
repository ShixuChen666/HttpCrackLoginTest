import requests
import base64

import base64Util

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'http://192.168.18.1',
    'Referer': 'http://192.168.18.1/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'content-type': 'application/json',
}

data = {
        "ver": "v1",
        "sid": "00000000000000000000000000000000",
        "method": "login",
        "param": {
            "msg_id": 11111,
            "params": [
                {
                    "module": "login",
                    "api": "login",
                    "param": {
                        "password": "MjEzNA=="
                    }
                }
            ]
        }
    }


def login(password):
    data["param"]["params"][0]["param"]["password"] = base64Util.base64decode(password)
    response = requests.post('http://192.168.18.1/zapi', headers=headers, json=data, verify=False)
    if response.is_redirect == True:
        print(password)
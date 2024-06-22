import json

import requests

host = "http://192.168.18.1"
uri = "/zapi"
port = 80
heads = {
    "Content-Type":"application/json"
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
          "password": "MQ=="
        }
      }
    ]
  }
}
response = requests.post(host+uri,headers=heads,json=data)
print(response)
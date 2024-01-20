# -*- coding: utf-8 -*-
# @Time    : 2024/1/20 11:33 AM
# @Author  : tianpeng
# @FileName: mock_data

import requests
from faker import Faker

url = "http://127.0.0.1:8000/auth/register/"
faker_tool = Faker()

for i in range(100000):
    payload = {'username': f'{faker_tool.first_name()}',
               'password': 'abc123456zx',
               'password2': 'abc123456zx',
               'email': f'{faker_tool.email()}',
               'first_name': 't',
               'last_name': 'p'}

    response = requests.request("POST", url, data=payload, timeout=5, headers={})
    print(response.text)

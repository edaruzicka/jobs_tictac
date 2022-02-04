import requests
import json

import configparser

config = configparser.ConfigParser()
config.read('account.conf')
acc_info = config['acc_info']
email = acc_info['email']
nickname = acc_info['nickname']

data = {
    'nickname':nickname, 
    'email':email}

r = requests.post('https://piskvorky.jobs.cz/api/v1/user', json=data)
print(r.json())

import requests

import configparser

config = configparser.ConfigParser()
config.read('account.conf')
acc_info = config['acc_info']
email = acc_info['email']
nickname = acc_info['nickname']

r = requests.post('https://piskvorky.jobs.cz/api/v1/user')
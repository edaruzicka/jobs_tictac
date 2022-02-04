import configparser

config = configparser.ConfigParser()
config.read('account.conf')
acc_info = config['acc_info']
user_id = acc_info['user_id']
user_token = acc_info['user_token']

print(f"{user_id} {user_token}")
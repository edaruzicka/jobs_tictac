import configparser

config = configparser.ConfigParser()
config.read('account.conf')
acc_info = config['acc_info']
email = acc_info['email']

print(email)
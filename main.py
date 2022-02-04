import configparser
from re import X
from tkinter import Y
import requests
import json

config = configparser.ConfigParser()
config.read('account.conf')
acc_info = config['acc_info']
user_id = acc_info['user_id']
user_token = acc_info['user_token']

def connect(user_token):
    r = requests.post('https://piskvorky.jobs.cz/api/v1/connect', json = {'userToken':user_token})

    json_response = r.json()
    print(json_response)

    game_token = json_response['gameToken']
    game_id = json_response['gameId']

    print(f"{game_token} {game_id}")

    return game_token, game_id

def play(user_token, game_token, x, y):
    r = requests.post('https://piskvorky.jobs.cz/api/v1/play', json = {'userToken':user_token, 'gameToken':game_token, 'positionX':x, 'positionY':y})
    json_response = r.json()
    print(json_response)

    return

def check_status(user_token, game_token):
    r = requests.post('https://piskvorky.jobs.cz/api/v1/checkStatus', json = {'userToken':user_token, 'gameToken':game_token})
    json_response = r.json()
    print(json_response)

    return

def check_last_status(user_token, game_token):
    r = requests.post('https://piskvorky.jobs.cz/api/v1/checkLastStatus', json = {'userToken':user_token, 'gameToken':game_token})
    json_response = r.json()
    print(json_response)

    player_id = json_response['coordinates']['playerId']
    x = json_response['coordinates']['x']
    y = json_response['coordinates']['y']

    return

def main():
    print(f"{user_id} {user_token}")

    game_token, game_id = connect(user_token)

if __name__ == "__main__":
    main()
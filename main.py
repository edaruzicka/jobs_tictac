import requests
import configparser
import json
import time

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
    code = json_response['statusCode']

    if code == 429:
        return None, None

    actual_player_id = json_response['actualPlayerId']
    winner_id = json_response['winnerId']

    return actual_player_id, winner_id

def check_last_status(user_token, game_token):
    r = requests.post('https://piskvorky.jobs.cz/api/v1/checkLastStatus', json = {'userToken':user_token, 'gameToken':game_token})
    json_response = r.json()
    print(json_response)
    code = json_response['statusCode']

    if code == 429:
        return None, None, None

    actual_player_id = json_response['actualPlayerId']

    if actual_player_id == user_id:
        x = json_response['coordinates'][0]['x']
        y = json_response['coordinates'][0]['y']
        return actual_player_id, x, y
    else:
        return actual_player_id, None, None

def main():
    print(f"{user_id} {user_token}")

    game_token, game_id = connect(user_token)
    winner_id = None

    while winner_id == None:
        time.sleep(5)

        actual_player_id, winner_id = check_status(user_token, game_token)

        time.sleep(5)

        if actual_player_id == user_id:
            print('MY TURN')
            actual_player_id, x, y = check_last_status(user_token, game_token)
            x = x + 1
            play(user_token, game_token, x, y)
        else:
            print('waiting...')
            #actual_player_id, x, y = check_last_status(user_token, game_token)
            


if __name__ == "__main__":
    main()
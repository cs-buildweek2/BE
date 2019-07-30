from app.models import Rooms, Exits
import requests
import time

def roomRequest(direction):
    secret = config('USER_KEY')
    URL = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/move/'
    headerOptions = {
        'Authorization': f'Token {secret}',
        'Content-Type': 'application/json'
    }
    request = {
        "direction": direction
    }
    response = requests.post(url = URL, headers = headerOptions, json = request)
    return response.json()

def initialization():
    secret = config('USER_KEY')
    URL = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/'
    headerOptions = {
        'Authorization': f'Token {secret}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url = URL, headers = headerOptions)
    return response.json()

def traverseMap():
    starting_room = initialization()
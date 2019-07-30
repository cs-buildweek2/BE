from app.models import Rooms, Exits
import requests

# curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"direction":"n"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/move/

def roomRequest(direction):
    secret = config('USER_KEY')
    URL = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/move/'
    headers = {
        'Authorization': f'Token {secret}'
    }
    data = {
        "direction": direction
    }

def traverseMap():
    #
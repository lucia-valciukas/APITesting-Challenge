import json

import requests


def first_try():
    url = "https://pokeapi.co/api/v2/berry/Cheri Berry"
    response = requests.get(url)
    response.json()




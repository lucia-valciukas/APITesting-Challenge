import json

import requests


def test_first_try():
    url = "https://pokeapi.co/api/v2/berry/3/"
    response = requests.get(url)
    data = response.json()
    assert data["firmness"] == {'name': 'very-soft', 'url': 'https://pokeapi.co/api/v2/berry-firmness/1/'}, "It Does Match"
  
def guardar_en_file(response):
      output_filename = "output_data.json"
      with open(output_filename, 'w') as json_file:
        json.dump(response, json_file, indent=4)




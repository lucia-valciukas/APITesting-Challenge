import json
import pytest

import requests
#se devuelven todas las funciones con nombre test_* o *_test 

#Función para guardar el archivo en cada test
#  me permite chequear manualmente que el resultado sea lo que yo programé 
def save_file(response, name_file):
      with open(name_file, 'w') as json_file:
        json.dump(response, json_file, indent=4)

#test con acceso claves-valor directos (sin más pares clave valor de hijos)
def test_berries_growth_time():
    url = "https://pokeapi.co/api/v2/berry/1/"
    response = requests.get(url)
    data = response.json()
    save_file(data,"berries_growth_time1")
    #validación básica con operadores lógicos :D 
    # el mensaje te salta cuando sale mal el test :D lo aprendí como al tercerintento
    assert data["growth_time"] == 3, "It Does NOT Match"

#test combinando asserts con otras funciones
def test_berries_growth_time_diferent():
    url = "https://pokeapi.co/api/v2/berry/2/"
    response = requests.get(url)
    data = response.json()
    save_file(data,"berries_growth_time2")
    assert isinstance(data["growth_time"],int), "It Does NOT Match"

#test con acceso claves-valor de hijos que no son listas
def test_berries_firmness():
    url = "https://pokeapi.co/api/v2/berry/3/"
    response = requests.get(url)
    data = response.json()
    save_file(data,"berries_growth_time3")
    assert data["firmness"]["name"] == 'very-soft', "It Does NOT Match"  

#test con listas en json 
def test_berries_flavor_lists():
    url = "https://pokeapi.co/api/v2/berry/3/"
    response = requests.get(url)
    data = response.json()
    save_file(data,"berries_growth_time4")
    assert data["flavors"][1]["flavor"]["name"] == 'dry', "It Does NOT Match" 

#test exceptions 

#test status codes 





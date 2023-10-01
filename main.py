import requests

token = "a8fbf2385ba5c2205a553a724b470624"
'''response = requests.post("https://api.pokemonbattle.me:9104/trainers/reg", json={ 
    "trainer_token": token,
    "email": "111german@dolnikov.ru",
    "password": "11Iloveqa1"}, headers = {"Content-Type":"application/json"})
print(response.text) 

response_activation = requests.post("https://api.pokemonbattle.me:9104/trainers/confirm_email",
                                    json={"trainer_token": token}, headers = {"Content-Type":"application/json"})
print(response_activation.text)''' 

response = requests.post("https://api.pokemonbattle.me:9104/pokemons",
                                    json={"name": "Бульбазавр",
                                         "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
                                    headers = {"trainer_token": token,"Content-Type":"application/json"})
print(response.text)

response = requests.put("https://api.pokemonbattle.me:9104/pokemons",
                                    json={"pokemon_id": "11672",
                                        "name": "Pompi"},
                                    headers = {"trainer_token": token,"Content-Type":"application/json"})
print(response.text)

response = requests.post("https://api.pokemonbattle.me:9104//trainers/add_pokeball",
                                    json={"pokemon_id": "11672"},
                                    headers = {"trainer_token": token,"Content-Type":"application/json"})
print(response.text)
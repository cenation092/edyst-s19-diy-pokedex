from bs4 import BeautifulSoup
import simplejson as json
import requests

# this script runs automatically at a period of 12 hours using crontab

def scrape():
    # array to store all pokemon data
    pokemon_data = [] 
    i = 1
    while i < 152:
        current_pokemon_data = {} # dictionary for storing current pokemon data with id = i
        URL = "https://pokeapi.co/api/v2/pokemon/" + (str)(i) # API of current pokemon
        response = requests.get(url = URL) # get request
        responseData = response.json() # convert data into json format

        #extract required data
        current_pokemon_data['id'] = responseData['id']
        current_pokemon_data['name'] = responseData['name']
        current_pokemon_data['sprite'] = responseData['sprites']['back_default']

        #append it to pokemon_data array
        pokemon_data.append(current_pokemon_data)
        i = i + 1
    # open file to store pokemon_data
    json_file = open('pokemonData.json', 'w')
    json.dump(pokemon_data, json_file) # convert data into json and dump into file
    json_file.close()

if __name__ == "__main__":
    scrape()

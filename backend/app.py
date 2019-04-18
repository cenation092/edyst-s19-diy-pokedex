import json
import requests
from flask import Response
from flask import Flask, render_template

# Instance of the Flask class for the API
app = Flask(__name__)

# Error handeler for invalid pokemon id
@app.errorhandler(500)
def page_not_found_500(e):
    return render_template('404.html'), 500

# Error handeler for invalid route
@app.errorhandler(404)
def page_not_found_404(e):
	return render_template('404.html'), 404

# Routing for valid pokemon id , Example: http://127.0.0.1:8006/api/pokemon/1
@app.route('/api/pokemon/<int:num>')
def index(num):
	required_pokemon = {}
	with open('pokemonData.json') as pokemonData: # open pokemonData.json file for extracting required pokemon data
		pokemon_data_in_json = json.load(pokemonData) # read file data
		required_pokemon['pokemon'] = pokemon_data_in_json[num-1] # extract required pokemon data
		required_pokemon_in_json =  json.dumps(required_pokemon) # convert data in JSON
		return required_pokemon_in_json 

if __name__ == '__main__':
    app.run(port=8006)
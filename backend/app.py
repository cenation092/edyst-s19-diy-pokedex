import json
import requests
from flask import Response
from flask import Flask, render_template

# Instance of the Flask class for the API
app = Flask(__name__)

# Error handeler for invalid pokemon id
@app.errorhandler(500)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handeler for invalid route
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# Routing for valid pokemon id , Example: http://127.0.0.1:8006/api/pokemon/1
@app.route('/api/pokemon/<int:num>')
def index(num):
	data = {} # dictonary for holding required pokemon data
	URL = "https://pokeapi.co/api/v2/pokemon/" # external API to get data of required pokemon
	URL = URL + str(num) # Add req Id of pokemon to the external API
	response = requests.get(url = URL) # request for getting data of requred pokemon
	responseData = response.json() # convert the data into JSON

	# Extract useful information from data which is provide by the external API
	data['id'] = responseData['id'] 
	data['name'] = responseData['name']
	data['sprite'] = responseData['sprites']['back_default']

	# dictonary to hold whole pokemon
	pokemon = {}
	pokemon['pokemon'] = data

	#convert whole data into JSON
	json_data = json.dumps(pokemon)

	#return required data 
	return json_data


if __name__ == '__main__':
    app.run(port=8006)
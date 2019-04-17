This repo contains **API** that return the details about the pokémons of the required **ID**.

 ## How to set up the project environemnt

* [Clone](https://github.com/cenation092/edyst-s19-diy-pokedex.git) this repo in your local machine.
* [Install](https://blog.ruanbekker.com/blog/2018/11/27/python-flask-tutorial-series-create-a-hello-world-app-p1/) python3 and flask. 
* Setup [virtual environment](https://blog.ruanbekker.com/blog/2018/12/09/python-flask-tutorial-series-setup-a-python-virtual-environment-p2/) in backend folder.
* Install all required packages mentioned in requirement.txt

 ## How to run the project
    
* Run the app.py
* Write this ( http://127.0.0.1:8006/api/pokemon/id )in you browser to get the details of required pokemon id in JSON format where `id` varies from `1 to 807` and here **port** is `8006` and **route** is `/api/pokemon/<int:id>`.

## If run in postman:

![image](https://user-images.githubusercontent.com/21224753/56210806-38631080-6074-11e9-94ce-a5bea59b0917.png)

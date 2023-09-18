from flask import Flask, render_template
import urllib.request, json

app_Rick = Flask(__name__)

@app_Rick.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character" 
    response = urllib.request.urlopen(url) 
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])

@app_Rick.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url) 
    data = response.read()
    dict = json.loads(data)

    return render_template("profile.html", profile=dict)


@app_Rick.route("/lista")
def get_list_characters():

    url = "https://rickandmortyapi.com/api/character" #indicação de onde abrir
    response = urllib.request.urlopen(url) # abertura
    characters = response.read() #ler resultado
    dict = json.loads(characters) #dicionário que irá receber a lista de personagens

    characters = []

    for character in dict["results"]:
        character = {
            "name": character["name"],
            "status": character["status"],
            "species": character["species"],
        }

        characters.append(character)
    
    return {"characters":characters}

@app_Rick.route("/location")
def get_list_location():

    url = "https://rickandmortyapi.com/api/location" 
    response = urllib.request.urlopen(url) 
    location = response.read() 
    dict = json.loads(location) 

    location = []

    for loc in dict["results"]:
        loc = {
            "name": loc["name"],
            "type": loc["type"],
            "dimension": loc["dimension"]
        }

        location.append(loc)
    
    return render_template("location.html", location=dict["results"])

@app_Rick.route("/episode")
def get_list_episode():

    url = "https://rickandmortyapi.com/api/episode" 
    response = urllib.request.urlopen(url) 
    episode = response.read() 
    dict = json.loads(episode) 

    episode = []

    for ep in dict["results"]:
        ep = {
            "id": ep["id"],
            "cod": ep["episode"],
            "name": ep["name"],
            "air_date": ep["air_date"]
            
        }

        episode.append(ep)
    
    return render_template("episode.html", episode=dict["results"])

@app_Rick.route("/episode/<id>")
def get_episode_id(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url) 
    data = response.read()
    dict = json.loads(data)

    return render_template("episode.html", episode=dict)

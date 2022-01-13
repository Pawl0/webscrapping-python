import sys
sys.path.append('./app/helpers')
sys.path.append('./app/epic')
sys.path.append('./app/kabum')
sys.path.append('./app/prime_game')
from helpers import openJsonFile
from epic import main as epicMain
from kabum import main as kabumMain
from prime_game import main as primeMain
from flask import Flask, jsonify

app = Flask(__name__)

cache = {
    "epic": "epic/epic-free-games.json",
    "kabum": "kabum/kabum-top-10.json",
    "prime": "amazon-prime-free-games.json"
}

@app.route("/epic")
def epic():        
    return jsonify(epicMain())

@app.route("/epic/cache")
def epicCache():        
    return jsonify(openJsonFile(cache["epic"]))

@app.route("/kabum")
def kabum():
    return jsonify(kabumMain())

@app.route("/kabum/cache")
def kabumCache():        
    return jsonify(openJsonFile(cache["kabum"]))

@app.route("/prime_game")
def prime():
    return jsonify(primeMain())

@app.route("/prime_game/cache")
def primeCache():        
    return jsonify(openJsonFile(cache["prime"]))
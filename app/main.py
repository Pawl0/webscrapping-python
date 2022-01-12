import sys
sys.path.append('./app/helpers')
sys.path.append('./app/epic')
sys.path.append('./app/kabum')
sys.path.append('./app/prime_game')
from epic import main as epicMain
from kabum import main as kabumMain
from prime_game import main as primeMain
from flask import Flask, jsonify

app = Flask(__name__)

cache = {
    "epic": [],
    "kabum": [],
    "prime": []
}

@app.route("/epic")
def epic():        
    cache["epic"] = epicMain()
    return jsonify(cache["epic"])

@app.route("/epic/cache")
def epicCache():        
    return jsonify(cache["epic"])

@app.route("/kabum")
def kabum():
    cache["kabum"] = kabumMain()
    return jsonify(cache["kabum"])

@app.route("/kabum/cache")
def kabumCache():        
    return jsonify(cache["kabum"])

@app.route("/prime_game")
def prime():
    cache["prime"] = primeMain()
    return jsonify( cache["prime"])

@app.route("/prime_game/cache")
def primeCache():        
    return jsonify(cache["prime"])
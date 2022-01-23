import sys
sys.path.append('./app/helpers')
sys.path.append('./app/factories')
from flask import Flask, jsonify
from helpers import openJsonFile
from WebscrapperFactory import makeWebscrapper

app = Flask(__name__)

cache = {
    "epic": "epic-free-games.json",
    "kabum": "kabum-top-10.json",
    "prime": "amazon-prime-free-games.json"
}

@app.route("/")
def home():
    return "<h1>Welcome to free games API</h1>"

@app.route("/epic")
def epic():        
    epicWebscrapper = makeWebscrapper["epic"]()
    return jsonify(epicWebscrapper.execute())

@app.route("/epic/cache")
def epicCache():        
    return jsonify(openJsonFile(cache["epic"]))

@app.route("/kabum")
def kabum():
    kabumWebscrapper = makeWebscrapper["kabum"]()
    return jsonify(kabumWebscrapper.execute())

@app.route("/kabum/cache")
def kabumCache():        
    return jsonify(openJsonFile(cache["kabum"]))

@app.route("/prime")
def prime():
    primeWebscrapper = makeWebscrapper["prime"]()
    return jsonify(primeWebscrapper.execute())

@app.route("/prime/cache")
def primeCache():        
    return jsonify(openJsonFile(cache["prime"]))

if __name__ == "__main__":
  app.run()
import sys
sys.path.append('./app/helpers')
sys.path.append('./app/factories')
from flask import Flask, jsonify
from helpers import openJsonFile
from WebscrapperFactory import WebscrapperFactory
from helpers import DriverManager

app = Flask(__name__)
driverManager = DriverManager()
webscrapperFactory = WebscrapperFactory(driverManager)
makeWebscrapper = webscrapperFactory.makeWebscrapper

cache = {
    "epic": "epic-free-games.json",
    "kabum": "kabum-top-10.json",
    "prime": "amazon-prime-free-games.json",
    "indiegala": "indiegala.json",
    "epicV": "epic-v.json",
}

@app.route("/")
def home():
    return "<h1>Welcome to free games API</h1>"

@app.route("/close")
def closeDriver():
    driverManager.close()
    return "Driver closed"

@app.route("/open")
def openDriver():
    driverManager.open()
    return "Driver open"

@app.route("/epic")
def epic():        
    epicWebscrapper = makeWebscrapper("epic")
    return jsonify(epicWebscrapper.execute())

@app.route("/epic/cache")
def epicCache():        
    return jsonify(openJsonFile(cache["epic"]))

@app.route("/kabum")
def kabum():
    kabumWebscrapper = makeWebscrapper("kabum")
    return jsonify(kabumWebscrapper.execute())

@app.route("/kabum/cache")
def kabumCache():        
    return jsonify(openJsonFile(cache["kabum"]))

@app.route("/prime")
def prime():
    primeWebscrapper = makeWebscrapper("prime")
    return jsonify(primeWebscrapper.execute())

@app.route("/prime/cache")
def primeCache():        
    return jsonify(openJsonFile(cache["prime"]))

@app.route("/indiegala")
def indiegala():
    indiegalaWebscrapper = makeWebscrapper("indiegala")
    return jsonify(indiegalaWebscrapper.execute())

@app.route("/indiegala/cache")
def indiegalaCache():        
    return jsonify(openJsonFile(cache["indiegala"]))

@app.route("/epic_v")
def epicV():
    epicVWebscrapper = makeWebscrapper("epicV")
    return jsonify(epicVWebscrapper.execute())

@app.route("/epic_v/cache")
def epicVCache():        
    return jsonify(openJsonFile(cache["epicV"]))

if __name__ == "__main__":
  app.run()
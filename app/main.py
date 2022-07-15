import sys
sys.path.append('./app/helpers')
sys.path.append('./app/factories')
sys.path.append('./app/infra/db')
from flask import Flask, jsonify
from helpers import openJsonFile, saveJsonFile
from WebscrapperFactory import WebscrapperFactory
from MongoClient import getMany

app = Flask(__name__)
webscrapperFactory = WebscrapperFactory()
makeWebscrapper = webscrapperFactory.makeWebscrapper

@app.route("/")
def home():
    return "<h1>Welcome to free games API</h1>"

@app.route("/epic")
def epic():        
    epicWebscrapper = makeWebscrapper("epic")
    return jsonify(epicWebscrapper.execute())

@app.route("/epic/cache")
def epicCache():        
    result = getMany("epic")
    return jsonify(result)

@app.route("/kabum")
def kabum():
    kabumWebscrapper = makeWebscrapper("kabum")
    return jsonify(kabumWebscrapper.execute())

@app.route("/kabum/cache")
def kabumCache():        
    result = getMany("kabum")
    return jsonify(result)

@app.route("/prime")
def prime():
    primeWebscrapper = makeWebscrapper("prime")
    return jsonify(primeWebscrapper.execute())

@app.route("/prime/cache")
def primeCache():        
    result = getMany("prime_game")
    return jsonify(result)

@app.route("/indiegala")
def indiegala():
    indiegalaWebscrapper = makeWebscrapper("indiegala")
    return jsonify(indiegalaWebscrapper.execute())

@app.route("/indiegala/cache")
def indiegalaCache():        
    result = getMany("indiegala")
    return jsonify(result)

@app.route("/epic_v")
def epicV():
    epicVWebscrapper = makeWebscrapper("epicV")
    return jsonify(epicVWebscrapper.execute())

@app.route("/epic_v/cache")
def epicVCache():        
    result = getMany("epic_v")
    return jsonify(result)

@app.route("/all")
def getAll():
    platformsDict = {
        "epic": "",
        "epicV": "",
        "prime": "",
        "kabum": "",
        "indiegala": "",
    }
    
    for platform in platformsDict:
        platformsDict[platform] = makeWebscrapper(platform).execute()
    
    saveJsonFile("all_platforms", platformsDict)
    return jsonify(platformsDict)

if __name__ == "__main__":
  app.run()
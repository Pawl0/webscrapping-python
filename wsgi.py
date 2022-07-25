from app.main import app
from WebscrapperFactory import WebscrapperFactory
import time
from apscheduler.schedulers.background import BackgroundScheduler

webscrapperFactory = WebscrapperFactory()
makeWebscrapper = webscrapperFactory.makeWebscrapper

def runAll():
    print("running all scrappers")
    scrappers = [
        "epic",
        "epicV",
        "prime",
        "kabum",
        "indiegala"
    ]
    for scrapper in scrappers:
        print(scrapper)
        makeWebscrapper(scrapper).execute()

if __name__ == "__main__":
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(runAll,'interval',hours=1)
    sched.start()
    app.run()
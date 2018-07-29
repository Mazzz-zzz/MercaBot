import json
import requests
import sqlite3
from datetime import datetime
import time


url = "https://mercatox.com/public/json24"
def getData():
    r = requests.get(url)
    data = json.loads(r.text)
    pairs = data["pairs"]
    return pairs
def getHydro(attribute):
    hydro = getData()["HYDRO_BTC"]
    return hydro[attribute]
def timeNow():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

con = sqlite3.connect("mercadata.db")
cur = con.cursor()

def pushToDatabase():
    cur.execute('''
                INSERT INTO HYDRO_BTC(Date, LastPrice, Low24Hour, High24Hour,
                PercentChange, BTC_Volume, LowAsk, HighBid)
                VALUES(?,?,?,?,?,?,?,?)
                ''',(timeNow(), getHydro("last"), getHydro("low24hr"), getHydro("high24hr"),
                 getHydro("percentChange"), getHydro("quoteVolume"), getHydro("lowestAsk"),getHydro("highestBid")))
for i in range(20):
    pushToDatabase()
    time.sleep(10)
    con.commit()
    print("Iteration: " + str(i))

con.close()

from fastapi import FastAPI
import requests
import redis

rediser = redis.Redis(host="localhost", port=6378, db=0)


app = FastAPI()


@app.get("/")
def read_root():
    return "Hellow World"

url: str = "https://api-american-football.p.rapidapi.com/teams"

headers = {
    'x-rapidapi-key': "3972cd314fmsh20cabddc424cfa8p1c0b68jsn12d25b55fccb",
    'x-rapidapi-host': "api-american-football.p.rapidapi.com"
}

@app.get("/american-football/fetch/{league}/{season}")
def read_user_details(league: str, season: str):
    # league: 1
    # season: 2023
    query = {"league":f"{league}","season":f"{season}"}
    results = requests.get(url=url, headers=headers, params=query)
    cache = rediser.get(league)
    if cache:
        print("cache hit")
    return results.json()


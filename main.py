from fastapi import FastAPI
import requests
import redis
import json
import pdb


# This initializes a connection to a local Redis instance, running on the 
# default port 6379 and using database 0
# The decode_responses=True ensures that Redis will automatically decode 
# the stored data from bytes to str.
rediser = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# app is an instance of FastAPI, which is used to define API routes and serve them.
app = FastAPI()

# This defines a basic route at the root ("/") of the API, 
# which returns the string "Hello World" when accessed via a GET request.
@app.get("/hello")
def read_root():
    return "Hellow World"

url: str = "https://api-american-football.p.rapidapi.com/teams"

headers = {
    'x-rapidapi-key': "3972cd314fmsh20cabddc424cfa8p1c0b68jsn12d25b55fccb",
    'x-rapidapi-host': "api-american-football.p.rapidapi.com"
}

# This route handles GET requests to the path 
# /american-football/fetch/{league}/{season}, 
# where league and season are dynamic path 
# parameters passed as part of the URL.
@app.get("/american-football/fetch/{league}/{season}")
def fetch_football_details(league: str, season: str):        
    # cache_key: The key used to store and retrieve data in Redis. 
    # It is generated based on the league and season to make each entry unique.
    # my_cache = rediser.get(cache_key): This checks if there is already cached 
    # data in Redis for the given league and season. If there is a cache hit, 
    # the value is assigned to my_cache.
    cache_key:str = f"league:{league}:season:{season}"
    my_cache = rediser.get(cache_key)
    
    # If cached data is found (my_cache is not None), 
    # it logs "cache hit" and returns the cached data after 
    # loading it from a string using json.loads().
    if my_cache:
        print("cache hit")
        return json.loads(str(my_cache))
    
    print("cache miss, fetching from API")
    query = {"league":f"{league}","season":f"{season}"}
    
    results = requests.get(url=url, headers=headers, params=query)
    
    # Store the response in Redis cache with an expiration time (e.g., 1 hour = 3600 seconds)
    rediser.setex(cache_key, 3600, json.dumps(results.json()))
    
    return results.json()


import pandas as pd
import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()

def getCoordinates(path,queryParams=dict()):
    url = f"https://api.foursquare.com/v2/venues/search"
    res = requests.get(url, params=queryParams)
    return res.json()
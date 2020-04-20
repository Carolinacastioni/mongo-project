import pandas as pd
import json
import requests
import numpy as np
import os
from dotenv import load_dotenv
load_dotenv()

def getFromFoursquare(coordinates,distance,name):
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
    client_id=os.getenv("CLIENT_APIKEY"),
    client_secret=os.getenv("SECRET_APIKEY"),
    v='20200401',
    ll= coordinates,
    radius= distance,
    query= name,
    )
    res = requests.get(url=url, params=params)
    return res.json()

starbucks = getFromFoursquare("40.757929,-73.985506,",500,"Starbucks")

lst = []
for i in range(starbucks['response']['totalResults']):
    lat = starbucks['response']['groups'][0]['items'][i]['venue']['location']['lat']
    long = starbucks['response']['groups'][0]['items'][i]['venue']['location']['lng']
    lst.append([lat,long])

df_starbucks = pd.DataFrame(lst) 
df_starbucks.columns = ["latitude", "longitude"]
df_starbucks["name"] = "Starbucks"

def getVeganFromFoursquare(coordinates,distance,category):
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
    client_id=os.getenv("CLIENT_APIKEY"),
    client_secret=os.getenv("SECRET_APIKEY"),
    v='20200401',
    ll= coordinates,
    radius= distance,
    categoryId= category,
    )
    res = requests.get(url=url, params=params)
    return res.json()

vegan = getVeganFromFoursquare("40.757929,-73.985506,",500,"4bf58dd8d48988d1d3941735")

lst_v = []
for i in range(vegan['response']['totalResults']):
    lat = vegan['response']['groups'][0]['items'][i]['venue']['location']['lat']
    long = vegan['response']['groups'][0]['items'][i]['venue']['location']['lng']
    lst_v.append([lat,long])

df_vegan = pd.DataFrame(lst_v) 
df_vegan.columns = ["latitude", "longitude"]
df_vegan["name"] = "Vegan Restaurants"

def getPartyFromFoursquare(coordinates,distance,category):
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
    client_id=os.getenv("CLIENT_APIKEY"),
    client_secret=os.getenv("SECRET_APIKEY"),
    v='20200401',
    ll= coordinates,
    radius= distance,
    categoryId= category,
    )
    res = requests.get(url=url, params=params)
    return res.json()

party = getPartyFromFoursquare("40.757929,-73.985506,",500,"4d4b7105d754a06376d81259")

lst_p = []
for i in range(len(party['response']['groups'][0]['items'])):
    lat = party['response']['groups'][0]['items'][i]['venue']['location']['lat']
    long = party['response']['groups'][0]['items'][i]['venue']['location']['lng']
    lst_p.append([lat,long])

df_party = pd.DataFrame(lst_p) 
df_party.columns = ["latitude", "longitude"]
df_party["name"] = "Nightlife Spot"

def getChildFromFoursquare(coordinates,distance,category):
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
    client_id=os.getenv("CLIENT_APIKEY"),
    client_secret=os.getenv("SECRET_APIKEY"),
    v='20200401',
    ll= coordinates,
    radius= distance,
    categoryId= category,
    )
    res = requests.get(url=url, params=params)
    return res.json()

child = getChildFromFoursquare("40.757929,-73.985506,",500,"5744ccdfe4b0c0459246b4c7")

lst_c = []
for i in range(child['response']['totalResults']):
    lat = child['response']['groups'][0]['items'][i]['venue']['location']['lat']
    long = child['response']['groups'][0]['items'][i]['venue']['location']['lng']
    lst_c.append([lat,long])

df_child = pd.DataFrame(lst_c) 
df_child.columns = ["latitude", "longitude"]
df_child["name"] = "Child service care"

df_requirements = pd.concat([df_starbucks,df_vegan,df_party,df_child], axis=0)
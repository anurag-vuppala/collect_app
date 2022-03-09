import requests
import os
import json
from twitter import *


cr = open('twitter_api.json')
crd = json.load(cr)

api_key = cr["API_KEY"]
api_sec = cr["API_SECRET"]
bearer_token = cr["BEARER"]




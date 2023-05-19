from os import read
from typing import Counter, Text
from numpy.__config__ import show
from numpy.lib.function_base import average
import pandas as pd
from pandas.core.dtypes.missing import notnull
from pandas.core.frame import DataFrame
import glob
from firebase_admin import firestore
import requests
import numpy as np
import matplotlib.pylab as plt
import matplotlib.image as img
from collections import OrderedDict
from datetime import datetime
from pprint import pprint


AUTH_URL = 'https://accounts.spotify.com/api/token'



# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': '',
    'client_secret': '',
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']


my_headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}


today = datetime.today()

# # ------------------
# Uncomment this part to get list of playlists from user >300 followers

id_list0={}
id_list={}
open('user_playlists_list.json', 'w').close()
url="https://api.spotify.com/v1/users/" + "43xzlwfo0tft7hn5r5e6dksrd" + "/playlists"
user_playlist_data=requests.get(url, headers=my_headers)
playlist_data_response_json= user_playlist_data.json()
print(len(playlist_data_response_json['items']))
for i in range(0, len(playlist_data_response_json['items'])):
    stri=str(playlist_data_response_json['items'][i]['external_urls'])
    playlist_id=stri[47:69]
    playlist_url= "https://api.spotify.com/v1/playlists/" + playlist_id
    playlist_info=requests.get(playlist_url, headers=my_headers)
    playlist_info_response_json= playlist_info.json()
    playlist_name=str(playlist_data_response_json['items'][i]['name'])
    print(playlist_info_response_json['followers']['total'])
    t1=  playlist_name[:30]+ " " + str(playlist_info_response_json['followers']['total'])
    if(playlist_info_response_json['followers']['total'] > 300):
        id_list[t1]= playlist_id
    
pprint(id_list)

    


  


        

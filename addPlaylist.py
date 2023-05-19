from os import read
from typing import Counter, Text
from numpy.__config__ import show
from numpy.lib.function_base import average
import pandas as pd
import json
from pandas.core.dtypes.missing import notnull
from pandas.core.frame import DataFrame
import glob
import firebase_admin 
import array
import requests
import numpy as np
import matplotlib.pylab as plt
import matplotlib.image as img
import string
from collections import OrderedDict
import base64
from datetime import datetime


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





print("Enter the genre")
genre_input=input()

print("Enter the Spotify URL")
spotify_url_input=input()
spotify_id=spotify_url_input[34:56]
print(spotify_id)

print("Enter instagram URL")
instagram_input=input()

print("Enter emaiL ID")
email_input=input()

print("Enter submission link")
submission_link_input=input()






url="https://api.spotify.com/v1/playlists/" + spotify_id
url3="https://api.spotify.com/v1/playlists/" + spotify_id +"/tracks"

playlist_data=requests.get(url, headers=my_headers)
playlist_data_response_json= playlist_data.json()


tracks_list = requests.get(url3, headers=my_headers)
tracks_list_response_json= tracks_list.json()





contact_list={}
contact_list['SpotifyID']=spotify_id

if(instagram_input == ""):
    contact_list['instagram']=instagram_input
else:
    contact_list['instagram']=str("https://www.instagram.com/")+instagram_input

contact_list['email']=email_input
contact_list['submissions']=submission_link_input
contact_list['refreshed_at']=str(today)
contact_list['added_to_pn_at']=str(today)





filename=genre_input + "_" + str(playlist_data_response_json['name'][:10]) + "_" + playlist_data_response_json['owner']['display_name'] + ".json"
print(filename)


with open(filename, "x") as f3:
     f3.write("[")
     f3.write(json.dumps(contact_list))


     
for i in range(0, len(playlist_data_response_json['tracks']['items'])):
    str2=str(playlist_data_response_json['tracks']['items'][i]['track']['uri'])
    url2= "https://api.spotify.com/v1/audio-features/" + str2[14:]

    playlist_audio_features = requests.get(url2, headers=my_headers)
    playlist_audio_features_json=playlist_audio_features.json()




    with open(filename, 'a') as f:
                f.write(",")
                f.write(json.dumps(playlist_audio_features_json, indent=4))

    
with open(filename, 'a') as f2:
    f2.write("]")




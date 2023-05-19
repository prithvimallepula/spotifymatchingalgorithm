from os import read
from typing import Counter, Text
from numpy.__config__ import show
from numpy.lib.function_base import average
import pandas as pd
import json
from pandas.core.dtypes.missing import notnull
from pandas.core.frame import DataFrame
import glob
import array
import requests
import numpy as np
import string
from collections import OrderedDict
import base64





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



# LLLLLL
# LLLLL


song_id='1Icw7fiD9uFGArRWJejXzV'

# LLLLLL
# LLLLLL

url2= "https://api.spotify.com/v1/audio-features/" + song_id
url3="https://api.spotify.com/v1/tracks/"+ song_id


      
artist_song_response = requests.get(url3, headers=my_headers)
artist_song_response_json= artist_song_response.json()


artist_song_audio_features = requests.get(url2, headers=my_headers)
artist_song_audio_features_json=artist_song_audio_features.json()

newpd=pd.DataFrame(artist_song_audio_features_json.items())



artist_danceability=newpd[1][0]
artist_energy=newpd[1][1]
artist_loudness=newpd[1][3]
artist_speechiness=newpd[1][5]
artist_acousticness=newpd[1][6]
artist_instrumentalness=newpd[1][7]
artist_liveness=newpd[1][8]
artist_valence=newpd[1][9]
artist_tempo=newpd[1][10]
artist_duration_ms=(newpd[1][16])




# print(playlist_response_json['name'])
# print(playlist_response_json['owner'])
# print(playlist_response_json['description'])
# print(playlist_response_json['followers'])
# print(playlist_response_json['external_urls'])
# print(playlist_response_json['images'])
# print(playlist_response_json['tracks']['items'][0]['added_at']) 

list1={}
list2={}
list3={}

added_at_list1={}


test={}


open('target2.json', 'w').close()
open('sorted.json', 'w').close()


for name in glob.glob('/Users/prithvimallepula/Desktop/PythonPratice/indie/indie_Alt*.json'):

    i=pd.read_json(name)
    url= "https://api.spotify.com/v1/playlists/" + i['SpotifyID'][0]
    url4="https://api.spotify.com/v1/playlists/" + i['SpotifyID'][0] + "/tracks"
    print(name)
    print("________________")

   

    danceability_mean=i['danceability'].mean()
    energy_mean=i['energy'].mean()
    key_mode=i['key'].mode()
    loudness_mean=i['loudness'].mean()
    speechiness_mean=i['speechiness'].mean()
    acousticness_mean=i['acousticness'].mean()
    instrumentalness_mean=i['instrumentalness'].mean()
    liveness_mean=i['liveness'].mean()
    valence_mean=i['valence'].mean()
    tempo_mean=i['tempo'].mean()
    duration_ms_mean=i['duration_ms'].mean()

    danceability_std=i['danceability'].std()
    energy_std=i['energy'].std()
    loudness_std=i['loudness'].std()
    speechiness_std=i['speechiness'].std()
    acousticness_std=i['acousticness'].std()
    instrumentalness_std=i['instrumentalness'].std()
    liveness_std=i['liveness'].std()
    valence_std=i['valence'].std()
    tempo_std=i['tempo'].std()
    duration_ms_std=i['duration_ms'].std()

    print("Mean")
    print("_________________")
    print("Dance: " + str(danceability_mean))
    print("Energy: "+str(energy_mean))
    print("loud: "+str(loudness_mean))
    print("speech: " +str(speechiness_mean))
    print("acoustic: " +str(acousticness_mean))
    print("instr: " +str(instrumentalness_mean))
    print("live: " +str(liveness_mean))
    print("valence: " +str(valence_mean))
    print("tempo: " +str(tempo_mean))
    print("duration: " +str(duration_ms_mean))

    print("Std Dev")
    print("_________________")
    print("Dance:" + str(danceability_std))
    print("Energy:"+str(energy_std))
    print("loud"+str(loudness_std))
    print("speech:" +str(speechiness_std))
    print("acoustic:" +str(acousticness_std))
    print("instr:" +str(instrumentalness_std))
    print("live:" +str(liveness_std))
    print("valence:" +str(valence_std))
    print("tempo:" +str(tempo_std))
    print("duration:" +str(duration_ms_std))






    danceability_max = danceability_mean + danceability_std
    danceability_min = danceability_mean - danceability_std

    energy_max = energy_mean+energy_std
    energy_min = energy_mean-energy_std

    loudness_max = loudness_mean + loudness_std
    loudness_min = loudness_mean - loudness_std

    speechiness_max = speechiness_mean + speechiness_std
    speechiness_min = speechiness_mean - speechiness_std

    acousticness_max = acousticness_mean + acousticness_std
    acousticness_min = acousticness_mean - acousticness_std

    instrumentalness_max = instrumentalness_mean + instrumentalness_std
    instrumentalness_min = instrumentalness_mean - instrumentalness_std

    liveness_max = liveness_mean + liveness_std
    liveness_min = liveness_mean - liveness_std

    valence_max = valence_mean + valence_std
    valence_min = valence_mean - valence_std

    tempo_max = tempo_mean + tempo_std
    tempo_min = tempo_mean - tempo_std

    duration_ms_max = duration_ms_mean + duration_ms_std
    duration_ms_min = duration_ms_mean - duration_ms_std

    counter=0
    a=0
    b=0
    c=0
    d=0
    
#     print("Danceability_max  " + str(danceability_max))
#     print("Danceability_min  " + str(danceability_min))
    

#     print("energy_max  " + str(energy_mean))
#     print("energy_min  "+str(energy_min))

#     print("loudness_max  " + str(loudness_max))
#     print("loudness_min  "+str(loudness_min))

#     print("speechiness_max  " + str(speechiness_max))
#     print("speechiness_min  "+str(speechiness_min))


#     print("acousticness_max  " + str(acousticness_max))
#     print("acousticness_min  "+str(acousticness_min))

#     print("instrumentalness_max  " + str(instrumentalness_max))
#     print("instrumentalness_min  "+str(instrumentalness_min))

#     print("valence_max  " + str(valence_max))
#     print("valence_min  "+str(valence_min))

#     print("tempo_max  " + str(tempo_max))
#     print("tempo_min  "+str(tempo_min))

#     print("duration_ms_max  " + str(duration_ms_max))
#     print("duration_ms_min  "+str(duration_ms_min))

    



    if(danceability_min<artist_danceability<danceability_max):
            counter=counter+10
            print("danceability: TRUE")
            
    

    if(energy_min<artist_energy<energy_max):
            counter=counter+10
            print("ENERGY: TRUE")
            
            


    if(loudness_min<artist_loudness<loudness_max):
            counter=counter+10
            ("LOUDNESS: TRUE")
            

    if(speechiness_min<artist_speechiness<speechiness_max):
            counter=counter+10
            b=b+1
            d=d+1
            print("SPEECHINESS TRUE")
            


    if(acousticness_min<artist_acousticness<acousticness_max):
            counter=counter+10
            a=a+1
            print("ACOUSTICNESS: TRUE")
            
            

    if(instrumentalness_min<artist_instrumentalness<instrumentalness_max):
            counter=counter+10
            a=a+1
            print("INSTRUMENTALNESS: TRUE")
            

    if(liveness_min<artist_liveness<liveness_max):
            counter=counter+10
            print("LIVENESS: TRUE")
           
            
            


    if(valence_min<artist_valence<valence_max):
            counter=counter+10
            print("VALENCE: TRUE")


    if(tempo_min<artist_tempo<tempo_max):
            counter=counter+10
            b=b+1
            c=c+1
            print("TEMPO: TRUE")
            
    
    if(duration_ms_min<artist_duration_ms<duration_ms_max):
            counter=counter+10
            print("DURATION: TRUE")
            


    

    if counter!=100 and a==1:
            counter=counter+1

    if counter!=100 and a==2:
            counter=counter+3

    if counter!=100 and b==1:
            counter=counter+2
    
    if counter!=100 and b==2:
            counter=counter+4
            
    if counter!=100 and c!=1:
            counter=counter-5

    if counter!=100 and d!=1:
            counter=counter-5  




            test[name]=counter
    

    playlist_response = requests.get(url, headers=my_headers)
    get_items = requests.get(url4, headers=my_headers)


    playlist_response_json=playlist_response.json()
    get_items_json=get_items.json()



    for p in range(0, len(playlist_response_json['tracks']['items'])):
        added_at_list1[p]=playlist_response_json['tracks']['items'][p]['added_at']

    # print(playlist_response_json)

    sorted_list=sorted(added_at_list1.items(), key=lambda p: p[1], reverse=True)
    if(counter!=100 and i['submissions'][0] != ''):
        counter=counter+2

    try:
        list1['match'] = counter
        list1['songname']=artist_song_response_json['name']
        list1['uri']=playlist_response_json['uri']
        list1['name'] = playlist_response_json['name']
        list1['external_urls'] = playlist_response_json['external_urls']
        list1['instagram']=i['instagram'][0]
        list1['email']=i['email'][0]
        list1['submissions']=i['submissions'][0]
        list1['owner'] = playlist_response_json['owner']
        list1['description'] = playlist_response_json['description']
        list1['followers'] = playlist_response_json['followers']
        list1['images'] = playlist_response_json['images']
        list1['latest_added_at'] = sorted_list[0][1]
        list1['total_items']=get_items_json['total']

        

    except:
        print("*******")
        print("Undefined playlist or issue with list1[] key-value pairs")
        print("********")





    with open('target2.json', 'r+') as f:
            if len(f.read()) == 0:
                f.write("[")
                f.write(json.dumps(list1, indent=4))


            else:
                with open('target2.json', 'a') as f1:
                    f1.write(",")
                    f1.write(json.dumps(list1, indent=4))
        

with open('target2.json', 'a') as f2:
        f2.write("]")
lst={}

with open('target2.json', 'r') as f3:
        data = json.load(f3)
        sorted_list2=sorted(data, key=lambda x: x['match'], reverse=True)
        with open('sorted.json', 'a') as f4:
                f4.write(json.dumps(sorted_list2, indent=4))
                f4.close()
                


        

# with open ('sorted.json', 'a') as f3:
#         f2.write




# # print(list2)
# # print(dict(sorted(list2.items(), key=lambda item: item[1], reverse=False)))

# #     with open("Target3.json", "r") as file:
# #      data = json.load(file)
     



    

    

# # # #     list2[name]=list1
# # # #     print(list2)
    








      

    

    


   









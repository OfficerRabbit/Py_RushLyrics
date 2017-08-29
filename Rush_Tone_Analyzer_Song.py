from watson_developer_cloud import ToneAnalyzerV3
from pprint import pprint
import json

url = "https://gateway.watsonplatform.net/tone-analyzer/api"
user_name = "6ee1a2e8-9d91-48d0-ba4d-629ac0180ddf"
pass_word = open('..\PyPass\PyKey\IBMWatson_API_Key.txt', 'r').read()
accept_type = "Content-type: application/json"

tone_analyzer = ToneAnalyzerV3(
    username = user_name,
    password = pass_word,
    version = '2017-08-27')

rush_album_data = open('.\Rush_Album_Lyrics.json', 'r').read()
rush_json = json.loads(rush_album_data)

song_album_score = {}

all_lyrics = ''

for idx, val in enumerate(rush_json['albums']['songs']):
    song_info = rush_json['albums']['songs'][idx]
    song_name = song_info['song name']
    song_lyrics = song_info['song lyrics']
    rush_song_tone = tone_analyzer.tone(song_lyrics, content_type='text/html')
    songc = rush_song_tone['document_tone']['tone_categories']
    all_lyrics = all_lyrics + song_lyrics
    
    song_score_dict = {}
    print(song_name)
    
    for songs in songc:
        song_score_dict[songs['category_name']] = {}
        print("\t" + songs['category_name'])
        current_songs_cat = songs['category_name']
        for song_score_type in songs['tones']:
            name = song_score_type['tone_name']
            val = song_score_type['score']
            song_score_dict[current_songs_cat][name] = val
            print("\t\t" + song_score_type['tone_name'] + ': ' + str(song_score_type['score']))

    rush_json['albums']['songs'][idx]['song analysis'] = song_score_dict
    

with open('.\Rush_Album_Analysis_JSON.json', 'w') as outfile:
    outfile.write(json.dumps(rush_json))

outfile.close()

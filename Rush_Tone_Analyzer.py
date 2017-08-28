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

"""
To get song names and lyrics from rush_json

tonec = rush_album_tone['document_tone']['tone_categories']

for song in rush_json['albums']['songs']:
    print(song['song name'])
    print(song['song lyrics'])

for tones in tonec:
	print(tones['category_name'])
	for score_type in tones['tones']:
		print("\t" + score_type['tone_name'] + ': ' + str(score_type['score']))

"""

rush_album_tone = tone_analyzer.tone(rush_json, content_type='text/html')

rush_album_tone_cat = {}

tonec = rush_album_tone['document_tone']['tone_categories']

tone_score_dict = {}

for tones in tonec:
    tone_score_dict[tones['category_name']] = {}
    print(tones['category_name'])
    current_tones_cat = tones['category_name']
    for score_type in tones['tones']:
        name = score_type['tone_name']
        val = score_type['score']
        tone_score_dict[current_tones_cat][name] = val
        print("\t" + score_type['tone_name'] + ': ' + str(score_type['score']))


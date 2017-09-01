import json
from pprint import pprint

with open('.\Rush_Full_Album_Tone_Analysis.json', 'r') as infile:
	rush_json = json.loads(infile.read())

rush_tone_data = {}

# Loop through albums
for idx, album in enumerate(rush_json['albums']):
    rush_tone_data['album name'] = album['album name']
    rush_tone_data['album info'] = album['album info']
    rush_tone_data['document_tone'] = album['album analysis']['document_tone']

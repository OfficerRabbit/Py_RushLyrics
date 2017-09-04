import json
from pprint import pprint

rush_album_data = open('.\Rush_Full_Album_Tone_Analysis.json', 'r').read()

rush_json = json.loads(rush_album_data)

total_tones = []

rush_album_emotions = {"albums":[]}

for alb_index, album in enumerate(rush_json['albums']):
    try:
        print("Album Name:",album['album name'])
        
        emotional_dict = {}
        emotional_dict['album name'] = album['album name']
        emotional_dict['tone scores'] = []
        
        rush_album_emotions['albums'].append(emotional_dict)
        album_tones = album['album analysis']['tone_categories'][0]['tones']
        
        for index, album_tone_category in enumerate(album['album analysis']['tone_categories'][0]['tones']):
            album_name = album['album name']
            
            tone_dict = {}
            tone_dict['tone name'] = album_tone_category['tone_name']
            tone_dict['tone score'] = album_tone_category['score']
            print(tone_dict)

            rush_album_emotions['albums'][alb_index]['tone scores'].append(tone_dict)

            
    except KeyError:
        pass


pprint(rush_album_emotions, indent=2)

with open('.\Rush_Full_Album_Emotions.json', 'w') as outfile:
    outfile.write(json.dumps(rush_album_emotions))

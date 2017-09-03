from watson_developer_cloud import ToneAnalyzerV3
from pprint import pprint
import json


url = "https://gateway.watsonplatform.net/tone-analyzer/api"
user_name = open('..\PyPass\PyUser\IBMWatson_API_User.txt', 'r').read()
pass_word = open('..\PyPass\PyKey\IBMWatson_API_Key.txt', 'r').read()
accept_type = "Content-type: application/json"

tone_analyzer = ToneAnalyzerV3(
     username = user_name,
     password = pass_word,
     version = '2017-08-27')

rush_album_data = open('.\Rush_Album_Lyrics.json', 'r').read()
rush_json = json.loads(rush_album_data)



"""
    This takes the X['document_tone']['tone_categories'] where X is a
    tone_analyzer.tone() object, which is a list.
"""
def clean_tone(list):
    pass


def separate_songs(rush_list_obj):
    for idx, val in enumerate(rush_list_obj):
        song_info = rush_json['albums']['songs'][idx]
        song_name = song_info['song name']
        song_lyrics = song_info['song lyrics']
        rush_song_tone = tone_analyzer.tone(song_lyrics,
                                            sentences=False,
                                            content_type='text/html')
        song_categories = rush_song_tone['document_tone']['tone_categories']
        all_lyrics = all_lyrics + song_lyrics
    
        song_score_dict = {}
        print(song_name)   


def analyze_album(rush_json_obj):
    rush_songs_list = rush_json_obj['albums']['songs']

    all_lyrics = ''

    separate_songs(rush_songs_list)

    
analyze_album()

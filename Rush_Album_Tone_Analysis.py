from watson_developer_cloud import ToneAnalyzerV3
from pprint import pprint
from watson_developer_cloud import WatsonException
import json

url = "https://gateway.watsonplatform.net/tone-analyzer/api"
user_name = open('..\PyPass\PyUser\IBMWatson_API_User.txt', 'r').read()
pass_word = open('..\PyPass\PyKey\IBMWatson_API_Key.txt', 'r').read()
accept_type = "Content-type: application/json"

tone_analyzer = ToneAnalyzerV3(
    username = user_name,
    password = pass_word,
    version = '2017-08-31')

rush_album_data = open('.\Rush_Full_Album_Data_Clean_JSON.json', 'r').read()

rush_json = json.loads(rush_album_data)

# Analyze each track
def analyze_track(song):
    global full_lyrics
    try:
        print("\tTrack:\t",song['track_title'])
        song_lyrics = song['track_lyrics']
        len(song_lyrics)
        full_lyrics = str(full_lyrics) + str(song_lyrics)
        lyric_analysis = tone_analyzer.tone(song_lyrics,
                                            content_type="text/html")
        
        song['song analysis'] = lyric_analysis['document_tone']
    except (ValueError, TypeError, WatsonException):
        pass

# Go through each track in an album to analyze
def parse_tracks(album):
    global full_lyrics
    print("Album:\t",album['album name'])
    full_lyrics = ''
    for idx, song in enumerate(album['album info']):
        analyze_track(song)

    #print(full_lyrics)
    try:
        full_lyrics_analysis = tone_analyzer.tone(full_lyrics,
                                                  content_type="text/html")
    except WatsonException:
        pass

    try:
        album['album analysis'] = full_lyrics_analysis['document_tone']
    except UnboundLocalError:
        pass
    

# Go through each album in file to parse tracks
def parse_album(rush_json):
    for idx, album in enumerate(rush_json['albums']):
        if idx == idx:
            #pprint(album, indent=2)
            parse_tracks(album)
        else:
            pass


parse_album(rush_json)

with open('.\Rush_Full_Album_Tone_Analysis.json', 'w') as outfile:
	outfile.write(json.dumps(rush_json))


outfile.close()

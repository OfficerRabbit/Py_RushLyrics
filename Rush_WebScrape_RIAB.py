import pprint
import time
import requests
import json
from bs4 import BeautifulSoup

rush_albums_list = open('.\Rush_Album_List_JSON.json', 'r').read()
rush_albums_json = json.loads(rush_albums_list)

original_name = ''

# Parse Rush file, for each album information in the file, send to 'connect_to_rush()'
def parse_file(rush_albums_json):
    # For every album name in the list, pass it to the connection
    for idx, album_info in enumerate(rush_albums_json['albums']):
        connect_to_rush(idx, album_info)

# Connect to Rush with the album name
def connect_to_rush(idx, album_info):
    original_album_name = album_info['album name']
    name = album_info['album name'].replace(' ','-')
    print('/' + name + '/' + album_info['site number'])
    album_url = name + '/' + album_info['site number']
    full_url = "http://www.rushisaband.com/rush/lyrics/" + album_url

    # Get Rush lyrics
    response = requests.get(full_url)

    # Soupify the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Pull tracks from Rush site
    tracks = soup.select('.track')
    
    # Clean tracks
    album_list = clean_tracks(tracks, idx)
    album_info['album info'] = album_list
    
    # Assign track info to dictionary
    # rush_albums_json['albums'][idx]['album info'] = total_track_info


# Clean track list
def clean_tracks(tracks, idx):
    album_list = []
    # For every track in the list, send it to the track_info()
    for idx, val in enumerate(tracks):
        total_track_info = track_info(idx, val)
        album_list.append(total_track_info)
    return album_list

# Create the information (title, number, length, lyrics) for each track
def track_info(idx, val):
    try:
        # Pulling track number, title, and time of first track
        track_title_length = val.find('h4').text
        track_headings = make_headings(track_title_length)
        track_lyrics = make_lyrics(val)
                
        # Add lyrics to track dictionary
        track_headings['track_lyrics'] = track_lyrics
        
        # Print the thing all pretty like!
        '''
        print("Track Number:\t" + track_headings['track_number'],
              "\nTrack Title:\t" + track_headings['track_title'],
              "\nTrack Length:\t" + track_headings['track_length'])
        print("Track Lyrics: \n" + track_headings['track_lyrics'])
        '''
        return track_headings
    except (UnboundLocalError, TypeError):
        pass

# Create the headings for each track
def make_headings(track_title_length):
    track_head_dict = {}
    # Checking to see whether the song title has a number, title, and length
    try:
        track_number = track_title_length[:track_title_length.index(')')]
        track_title = track_title_length[(track_title_length.index(')')+2):(track_title_length.index('(')-1)]
        track_length = track_title_length[(track_title_length.index('(')+1):(track_title_length.index(':')+3)]
    except (IndexError, ValueError) as error:
        print("Error on:\t" + track_title_length + "\nError Message:\n"+ str(error))
        pass

    # Assign dictionary values for number, title, and length
    track_head_dict['track_number'] = track_number
    track_head_dict['track_title'] = track_title
    track_head_dict['track_length'] = track_length
    
    return(track_head_dict)


def make_lyrics(val):
    try:
        # Remove the strings before this to get the lyrics
        up_partition = "[ Hide Lyrics ]"
        # Pull the lyrics and clean them up
        track_lyrics = val.getText(separator=' ').split(up_partition)[1]
        track_lyrics = track_lyrics.replace('\n', '').lstrip().rstrip().replace('  ', '. ')
        track_lyrics = track_lyrics.replace("[ Watch Video ]", '')
        return track_lyrics
    except (TypeError, IndexError):
        pass



# Run the whole she-bang
parse_file(rush_albums_json)

# Add it to new file
with open('.\Rush_Full_Album_Data_JSON.json', 'w') as outfile:
           outfile.write(json.dumps(rush_albums_json))

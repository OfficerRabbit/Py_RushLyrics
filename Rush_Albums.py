import urllib.request
import re
import pprint
import time
from bs4 import BeautifulSoup

# AZ Lyrics lookup I found online
def get_lyrics(artist,song_title):
    artist = artist.lower()
    song_title = song_title.lower()
    # remove all except alphanumeric characters from artist and song_title
    artist = re.sub('[^A-Za-z0-9]+', "", artist)
    song_title = re.sub('[^A-Za-z0-9]+', "", song_title)
    if artist.startswith("the"):    # remove starting 'the' from artist e.g. the who -> who
        artist = artist[3:]
    url = "http://azlyrics.com/lyrics/"+artist+"/"+song_title+".html"
    
    try:
        content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(content, 'html.parser')
        lyrics = str(soup)
        # lyrics lies between up_partition and down_partition
        up_partition = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
        down_partition = '<!-- MxM banner -->'
        lyrics = lyrics.split(up_partition)[1]
        lyrics = lyrics.split(down_partition)[0]
        lyrics = lyrics.replace('<i>[Chorus]</i>','').replace('<br>','').replace('</br>','').replace('<br/>','').replace('</div>','').strip()
        return lyrics
    except Exception as e:
        return "Exception occurred \n" +str(e)


# Rush lyrics page with all songs by album
url = "https://www.azlyrics.com/r/rush.html"

# Open and read the page
content = urllib.request.urlopen(url).read()

# BeautifulSoup html parse the content
content_bs = BeautifulSoup(content, 'html.parser')

# List all the Rush albums
albums = content_bs.select('.album')

# Remove the last list item that contains "Other Songs"
del albums[-1]

# Create empty list for Rush albums
rush_album_list = []

# Go through the 'albums' dict and pull out the clean album names
for x, val in enumerate(albums):
    album_name_raw = albums[x].getText()
    album_name = album_name_raw[7:]
    album_name = album_name.replace('"','')
    album_name_str = album_name[:(album_name.index('(')-1)]

    rush_album_list.append(album_name_str)
    
# Create dictionary
album_dict = {}
for album in rush_album_list:
    album_dict[album] = {'songs':[]}
    
# Album and Song part of html
alb_song_raw = content_bs.select('#listAlbum')
alb_song_raw = alb_song_raw[0].getText()
split_str = r'other songs'
alb_song = alb_song_raw.split(split_str)[0]

# Split lines out, remove blanks
album_key = ''
song_lines = alb_song.splitlines()
song_lines = filter(None, song_lines)

# Create a new dictionary for album names and songs
for line in song_lines:
    if line[:5] == 'album':
        album_year = line[(line.index('(')):(line.index('('))+5]
        album_key_raw = line[(line.index('"')):(line.index(' ('))]
        album_key = album_key_raw.replace('"','')
        album_dict[album_key]['year'] = album_year
    if line[:5] != 'album':
        album_dict[album_key]['songs'].append({line: ''})

album_dict = {'albums': album_dict}

# pprint.pprint(album_dict, indent=4)

for album in album_dict['albums']:
    for song in album_dict['albums'][album]['songs']:
        time.sleep(5)
        song = str(song)
        song_lyrics = get_lyrics('Rush', song)
        print(song)
        print(song_lyrics)
        album_dict['albums'][album]['songs'][0]['lyrics'] = song_lyrics


with open('.\Rush_Data_JSON.json', 'wb') as outfile:
    outfile.write()

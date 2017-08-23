import urllib.request
from bs4 import BeautifulSoup

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

    rush_album_list.append(album_name[:(album_name.index('(')-1)])

    # print(album_name)

# Create dictionary

rush_dict = {}

rush_dict.update({'albums': rush_album_list})
    
# Album and Song part of html
alb_song_raw = content_bs.select('#listAlbum')
alb_song_raw = alb_song_raw[0].getText()

split_str = r'other songs'

alb_song = alb_song_raw.split(split_str)[0]
album_key = ''

for line in alb_song.splitlines():    
    if line[:5] == 'album':
        album_key = line[line.index('"'):line.index('(')]
        album_key = album_key.replace('"','')
        # print(album_key)
        

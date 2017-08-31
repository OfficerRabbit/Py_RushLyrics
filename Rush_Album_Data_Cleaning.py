import json
import re
from pprint import pprint

rush_album_data =  open('.\Rush_Full_Album_Data_JSON.json', 'r').read()

rush_album_data = json.loads(rush_album_data)

#pprint(rush_album_data['albums'][], indent=2)

# Clean the lyrics
def clean_lyrics(track_lyrics, track):
    try:
        # Clean status indicator
        clean_status = False
        # Checking to see if first char is period, not sure how to have that in strip list
        if track_lyrics[0] == '.':
            new_lyrics = track_lyrics[1:].lstrip().rstrip()
            track['track_lyrics'] = new_lyrics
            #print(track['track_lyrics'])
            clean_status =+ True
        else:
            print(track['track_lyrics'])
            clean_status =+ False
    except TypeError:
            pass
        
    # This will be specific pieces I'm removing from the lyrics
    # I know which ones I need to remove so no regex for now, maybe later
    clean_list = [# Fly by Night
                  "III. Of The Battle i) Challenge And Defiance ii) 7/4 War Furor iii) Aftermath iv) Hymn of Triumph. IV. Epilogue",
                  "I. At The Tobes of Hades",
                  "II. Across The Styx ",
                  # Caress of Steel
                  "I. Into Darkness (4:12)",
                  "II. Under The Shadow (4:25) ",
                  "III. Return of the Prince (3:52) ",
                  "I. In the Valley (4:18)",
                  "II. Didacts and Narpets (1:00) ",
                  "III. No One at the Bridge (4:19) ",
                  "IV. Panacea (3:14) ",
                  "V. Bacchus Plateau (3:13) ",
                  "VI. The Fountain (3:49) ",
                  # 2112
                  "I. Overture (4:32) ",
                  "II. Temples of Syrinx (2:13) ",
                  "III. Discovery (3:29) ",
                  "IV. Presentation (3:42) ",
                  "V. Oracle: The Dream (2:00) ",
                  "VI. Soliloquy (2:21) ",
                  "VII. The Grand Finale (2:14)",
                  # A Farewell to Kings
                  "Prologue (5:01)",
                  "1. (0:45) ",
                  "2. (1:34) ",
                  "3. (3:05) ",
                  ]

    try:
        # For each clean item see if it's in the lyrics and remove
        for clean_item in clean_list:
            if clean_item in track_lyrics:
                new_lyrics = track['track_lyrics'].replace(clean_item, '')
                track['track_lyrics'] = new_lyrics.lstrip().rstrip()
                print("Item Cleaned:\t" + clean_item)
                print(track['track_lyrics'])
                clean_status =+ True
            else:
                clean_status =+ False
                pass
    except TypeError:
        pass

    if clean_status == 1:
        clean_status = True
    else:
        clean_status = False
    return clean_status


clean_album_list = []

# For every album in the rush_album_data file...
for idx, album in enumerate(rush_album_data['albums']):
    # Tester so I can work out the single run before making the loop
    
    if idx == 5:
        print("\nAlbum Name:\t" + album['album name'])
        # For every track in the album info...
        for idx, track in enumerate(album['album info']):
            print("\nTrack Number:\t" + track['track_number'])
            print("Track Title:\t" + track['track_title'])
            print("Track Length:\t" + track['track_length'])
            print("Track Lyrics:")
            clean_status = clean_lyrics(track['track_lyrics'], track)
            print("Clean Status:\t" + str(clean_status))
            clean_album_list.append(clean_status)
            #print(track['track_lyrics'] + "\n")
    else:
        pass

"""
print(clean_album_list)

if True in clean_album_list:
    print("*****\tStill Needs Cleaning\t*****")
else:
    print("*****\tAll Clean!!!\t*****")
"""

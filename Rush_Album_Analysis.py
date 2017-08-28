from Rush_Solo_Album_JSON import rush_solo
import re

total_list = []
cleaned_list = []

rush_songs = rush_solo['albums']['songs']
"""
def clean_word(dirty_word):
    cleaned_word = re.sub(r'[^\w]', '', dirty_word)
    cleaned_word = cleaned_word.replace(',','')
    cleaned_word = cleaned_word.replace('.','')
    cleaned_word = cleaned_word.title()
    return cleaned_word

def clean_list(word_list):
    for x in word_list:
        cleaned = clean_word(x)
        if cleaned in cleaned_list:
            pass
        else:
            cleaned_list.append(x)


def make_word_list():
    for x in rush_songs[0]['song lyrics'].split():
        if x in total_list:
            pass
        else:
            total_list.append(x)


def clean_rush_word():
    
    make_word_list()

    clean_list(total_list)


clean_rush_word()

print(cleaned_list)
"""

for x in rush_songs[0]['song lyrics'].split():
    if x in total_list:
        pass
    else:
        total_list.append(x)

for x in total_list:
    cleaned_word = re.sub(r'[^\w]', '', x)
    cleaned_word = cleaned_word.replace(',','')
    cleaned_word = cleaned_word.replace('.','')
    cleaned_word = cleaned_word.title()
    if cleaned_word in cleaned_list:
        pass
    else:
        cleaned_list.append(cleaned_word)


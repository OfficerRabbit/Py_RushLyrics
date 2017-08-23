import urllib.request
from bs4 import BeautifulSoup

# Rush lyrics page with all songs by album
url = "https://www.azlyrics.com/r/rush.html"

# Open and read the page
content = urllib.request.urlopen(url).read()

# BeautifulSoup html parse the content
content_bs = BeautifulSoup(content, 'html.parser')

# Output the html content to a local text file
with open('.\Rush_Lyric_List.html', 'wb') as outfile:
    outfile.write(content)

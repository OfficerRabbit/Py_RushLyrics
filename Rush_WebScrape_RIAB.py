import pprint
import time
import requests
from bs4 import BeautifulSoup

url = "http://www.rushisaband.com/rush/lyrics"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

albums = soup.select('#albumlist')

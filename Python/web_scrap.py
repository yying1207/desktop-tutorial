#<a href="https://example.com/page1">Link 1</a>
#<a href="https://example.com/page2">Link 2</a>
#<a href="https://example.com/page3">Link 3</a>

import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
links = [link['href'] for link in soup.find_all('a')]

print(links)
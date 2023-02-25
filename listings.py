import requests
from bs4 import BeautifulSoup
from constants import headers
from imagefetch import download_images

url = 'https://dolap.com/profil/'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
links = [link.get('href') for link in soup.find_all('a', {'rel': 'nofollow', 'href': lambda href: href and 'dolap.com/urun' in href})]

download_images(links)

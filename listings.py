import os
import requests
from bs4 import BeautifulSoup
from constants import headers
from imagefetch import download_images

user = ''
url = f'https://dolap.com/profil/{user}'
response = requests.get(url, headers=headers)

folder_name = user
soup = BeautifulSoup(response.content, 'html.parser')
links = [link.get('href') for link in soup.find_all('a', {'rel': 'nofollow', 'href': lambda href: href and 'dolap.com/urun' in href})]

download_images(links, folder_name)

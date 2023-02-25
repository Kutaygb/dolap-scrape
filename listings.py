from bs4 import BeautifulSoup
import requests
import os
from constants import headers
from imagefetch import download_images

page_num = 1
url = 'https://dolap.com/profil/'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
links = soup.find_all('a', {'rel': 'nofollow', 'href': lambda href: href and 'dolap.com/urun' in href})

image_urls = []
for link in links:
    image_urls.append(link.get('href'))

download_images(image_urls, headers)

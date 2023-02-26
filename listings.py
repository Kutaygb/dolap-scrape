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

pagination = soup.find('ul', {'class': 'pagination other'})
pages = [link.get('href') for link in pagination.find_all('a')]

for page in pages:
    page_url = f'https://dolap.com{page}'
    page_response = requests.get(page_url, headers=headers)
    page_soup = BeautifulSoup(page_response.content, 'html.parser')
    page_links = [link.get('href') for link in page_soup.find_all('a', {'rel': 'nofollow', 'href': lambda href: href and 'dolap.com/urun' in href})]
    links.extend(page_links)

download_images(links, folder_name)

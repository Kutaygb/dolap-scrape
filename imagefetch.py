import os
import time
import requests
from bs4 import BeautifulSoup

from constants import headers


def download_images(image_urls):
    downloaded_urls = set()
    for url in image_urls:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")

        for img in soup.find_all("img", src=lambda src: src and src.startswith("http") and src.endswith(".jpg")):
            src = img["src"]
            if src in downloaded_urls:
                continue
            filename = os.path.join("images", os.path.basename(src))
            with open(filename, "wb") as f:
                response = requests.get(src, headers=headers)
                f.write(response.content)
                print(f"{filename} saved.")
            downloaded_urls.add(src)
            time.sleep(1)

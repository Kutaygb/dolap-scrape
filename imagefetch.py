import requests
from bs4 import BeautifulSoup
import os
from constants import headers
import time

def download_images(image_urls, headers):
    downloaded_urls = set()
    for url in image_urls:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")

        img_tags = soup.find_all("img")
        for img in img_tags:
            if "src" in img.attrs:
                src = img["src"]
                if not src.startswith("http"):
                    continue
                if not src.endswith(".jpg"):
                    continue
                if src in downloaded_urls:
                    continue
                filename = os.path.join("images", src.split("/")[-1])
                with open(filename, "wb") as f:
                    response = requests.get(src, headers=headers)
                    f.write(response.content)
                    print(f"{filename} saved.")
                
                downloaded_urls.add(src)
                time.sleep(1)

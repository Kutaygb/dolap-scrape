import os
import time
import requests
import threading
from bs4 import BeautifulSoup
from constants import headers


def download_images(image_urls, folder_name):
    downloaded_urls = set()

    def download(url):
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")

        for img in soup.find_all("img", src=lambda src: src and src.startswith("http") and src.endswith(".jpg")):
            src = img["src"]
            if src in downloaded_urls:
                continue
            filename = os.path.basename(src)
            filepath = os.path.join("images", folder_name, filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, "wb") as f:
                response = requests.get(src, headers=headers)
                f.write(response.content)
                print(f"{filepath} saved.")
            downloaded_urls.add(src)

    threads = []
    for url in image_urls:
        t = threading.Thread(target=download, args=(url,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
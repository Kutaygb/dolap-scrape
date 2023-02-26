import os
import time
import requests
import concurrent.futures
from bs4 import BeautifulSoup
from constants import headers


def download_images(image_urls, folder_name):
    downloaded_urls = set()

    def download_image(url):
        nonlocal downloaded_urls
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

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(download_image, url) for url in image_urls]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Exception occurred: {e}")

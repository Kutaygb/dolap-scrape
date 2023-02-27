# Overview

This project consists of three files: `constants.py`, `imagefetch.py`, and `listings.py`.

`constants.py` file contains a dictionary with a User-Agent header, which is used to send HTTP requests to websites in a way that looks like it's coming from a web browser.

`imagefetch.py` file contains a function `download_images()` that downloads images from a list of URLs and saves them to a specified folder. It does this by first sending HTTP requests to the URLs using the headers from `constants.py`, then parsing the HTML content of the response to find image tags with URLs that end with ".jpg". It saves each image to a file using the filename from the URL and the specified folder name.

`listings.py` file imports `download_images()` function from `imagefetch.py` to download images from a user's listings on dolap.com. It first sends a GET request to the user's profile page using the headers from `constants.py`. It then parses the HTML content of the response to find links to the user's listings. It also finds pagination links and sends requests to each of those pages to get the listing links. It finally passes the list of listing links and the user's name to `download_images()` function to download and save the images.
Installation and Usage

Clone the repository to your local machine.

```bash
git clone https://github.com/<username>/<repository-name>.git
```

Install the required libraries.

```bash
pip install -r requirements.txt
```

Update the user variable in listings.py with the user whose listings you want to download.

```python
user = 'your-username'
```

Run listings.py.

```bash
python listings.py
```

The downloaded

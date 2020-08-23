# ba-webcam-scraper
Scraper to obtain training / test images from public parking lot webcams for my bachelor thesis

# Requirements
- Python 3.8.5
- pipenv

  `pip install pipenv`

# Installation and Setup
Install dependencies run

`pipenv install`

To change into projects virtual environment run

`pipenv shell`

Type `exit` or `CTRL + d` to exit virtual environment

# Usage
Inside virtual environment run

`scrapy crawl geierlay_webcam`

to run geierlay crawler (change name of crawler to use the other crawlers).
Images will be downloaded to the `images` folder

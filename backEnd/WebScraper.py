from bs4 import BeautifulSoup
import requests
import urllib

## using a keyboard website as an example
url = 'https://kbdfans.com/collections/new-arrival/products/kbd75-hot-swap-pcb-foam'
html = urllib.request.urlopen(url)
for line in html:
    print(line)
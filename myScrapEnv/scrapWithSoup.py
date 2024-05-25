# import required modules
from bs4 import BeautifulSoup
import requests

# Create a pool of proxies 
proxies = {
    "http": "185.244.210.185:80",
    "http": "49.13.161.231:80",
    "http": "72.10.164.178:5657",
    "http": "147.251.6.31:3128",
    "http": "72.10.160.174:4881",
    "http": "67.43.227.227:20627",
    "http": "72.10.160.90:32073",
    } 

url = 'https://en.wikipedia.org/wiki/Main_Page'

# get URL
page = requests.get(url, proxies=proxies)

# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')

# display scraped data
print(soup.prettify())

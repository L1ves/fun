from bs4 import BeautifulSoup
import re
import urllib3
import urllib
import os
import requests
import urllib.request

# Download parameters
image_type = 'Project'
movie = 'Avatar'
url = 'https://www.google.com/search?q="+movie+"&source=lnms&tbm=isch'
header = {'User-Agent': 'Mozilla/5.0'}
soup = urllib.request.urlopen(url)
print(soup.read())


import urllib.request
import urlopen
from bs4 import BeautifulSoup
import ssl
import re
total = 0
count = 0
numlist=list()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html =urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for line in tags:
    line=int(line.contents[0])
    count +=1
    total +=line
print(total)
print(count)

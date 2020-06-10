
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

url = input('Enter URL ')
html =urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')

count =int( input("Enter count:"))

position = int(input("Enter position:"))
n=0
url = tags[position].get('href', None)
while n < count:
    n = n + 1
    print ('Retrieving:', url)
    html =urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    url = tags[position].get('href', None)

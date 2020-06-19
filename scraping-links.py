
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
count = input('Enter count: ')
count = int(count)
position = input('Enter position: ')
position = int(position)
pos = 1
c = 1
print('Retreiving: ',url)
while c <= count:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        if pos == position :
            url = tag.get('href', None)
            print('Retreiving: ',url)
        pos = pos + 1
    c = c + 1
    pos = 1

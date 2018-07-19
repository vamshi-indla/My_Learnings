# Assignment to get the links and their links and so on
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
cnt = input('Enter count:')
pos = input('Enter position:')

for c in range(int(cnt)):

    # retrieve html
    html = urllib.request.urlopen(url, context=ctx).read()  
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all of the anchor tags
    tags = soup('a')
    count = 1
    
    # print the pos(3) position tag
    for tag in tags:
        if count == int(pos):
            url = tag.get('href', None)
            print(url)
            break
        count += 1     
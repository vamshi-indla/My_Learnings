# read a html file and sum up all the numbers inside that file table

# Sampe input:
# 
# 

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


import re
total = 0
num_list = re.findall('"comments">([0-9]+)',soup.decode())
for num in num_list:
    total = total + int((num))
print('Count %d' %len(num_list))
print('Sum %d' %total)
#Extracting Data from XML
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# sample input url: 
# http://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_117409.xml

url = input('Enter location: ')
print('Retrieving ', url)

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data.decode())
#lst = tree.findall('comments/comment')
lst = tree.findall('.//comment')

total = 0 
for item in lst:
    total += int(item.find('count').text)

print('Count:', len(lst))
print('Sum:', total) 
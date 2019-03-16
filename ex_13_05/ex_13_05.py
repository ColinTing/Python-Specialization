import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
if len(address) < 1: 
    address = 'http://py4e-data.dr-chuck.net/comments_187630.xml'

url = address
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

counts = tree.findall('.//count')
ct = 0
sum = 0
for count in counts:
    sum = sum + int(count.text)
    ct= ct +1
print("Count:", ct)
print("Sum:", sum)

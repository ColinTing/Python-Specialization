#深度优先搜索算法
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
if len(url)<1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Carter.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

sCount = input('Enter count:')
sPosition = input('Enter position:')
if len(sCount)<1 and len(sPosition)<1:
    sCount = '7'
    sPosition = '18'
count = int(sCount)
position = int(sPosition)
# Retrieve all of the anchor tags
tags = soup('a')
print("Retrieving:",url)
for i in range(0,count,1):
    url = tags[position-1].get('href',None)
    print("Retrieving:",url)
    name = re.findall('known_by_(.+).html',url)[0]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

print("last Name:",name)










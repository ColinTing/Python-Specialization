import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#忽略SSL证书错误
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter -:")
#http://www.dr-chuck.com/page2.htm
#read()表示阅读html中的东西,也可阅读json中的内容
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('a')
count = 0
for tag in tags:
    count= count+1
    print(tag.get('href',None))

print("total antor=", count)


from __future__ import unicode_literals
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"


conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()
#DROP TABLE IF EXISTS Locations (address TEXT, geodata TEXT) 报错
#Locations之后的内容要去掉
# cur.execute('''
# DROP TABLE IF EXISTS Locations''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0
for line in fh:
    #一次取完所有数据，不重启程序是非常不好的习惯，1.有bug查问题很难查找。2.没有运用科学方法做事，化繁就简
    if count > 200:
        print("已经获取了201条地址，要想获取更多请重启程序")
        break       
    address = line.strip()
    #address.encode()  刚刚竟然脑残的写成了address,encode()
    cur.execute('SELECT geodata FROM Locations WHERE address= ?',
        (memoryview(address.encode()),))
    try:
        #漏了一个括号fetchnone()，但我却一直以为等号要替换成like语句，因为在DB Browser for SQLite 中等于号查不到结果（这个找了好久）
        data = cur.fetchone()[0]
        #如果没有数据这里直接抛出异常，空值判断没有效果
        # if data is not None:
        #     print("数据已获取")
        print("数据已经获取",address)
        continue
    except:
        print("下一步调用Google地图API")

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)
        js = None
        continue
    #"status" = "ZERO_RESULTS"不代表调用次数用完了，所以判断需要加上js['status'] != 'ZERO_RESULTS'
    if not js or 'status' not in js or js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS':
        print('==== Failure To Retrieve ====')
        print(data)
        print(count)
        break
    
    print(json.dumps(js, ensure_ascii=False, indent=4))
    
    cur.execute('INSERT INTO Locations (address, geodata) VALUES (?,?)',
    (memoryview(address.encode()),memoryview(data.encode())))

    conn.commit()

    if count % 10 ==0:
        print('休息一下')
        time.sleep(5)

print('地址原始数据获取完成，之后运行数据可视化程序')
import urllib.request, urllib.parse, urllib.error
import json

while True:
    address = input('Enter location: ')
    if len(address) < 1: 
        address = 'http://py4e-data.dr-chuck.net/comments_187631.json'

    print('Retrieving', address)
    uh = urllib.request.urlopen(address)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    try: 
        js = json.loads(data)
    except:
        js = None

    if not js or 'note' not in js or js['note'] == '':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print(json.dumps(js,ensure_ascii=False,indent=4))
    count = 0
    sum = 0
    ct = 0
    for item in js['comments']:
        count = int(item['count'])
        sum = sum + count
        ct=ct+1
    print("Count:", ct)
    print("Sum:",sum)


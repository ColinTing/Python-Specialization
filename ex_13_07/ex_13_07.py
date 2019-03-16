from __future__ import unicode_literals
import urllib.request, urllib.parse, urllib.error
import json
import ssl

#忽略SSL证书错误
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'https://apis.map.qq.com/ws/geocoder/v1/?'
while True:
    address = input('Enter location: ')
    if len(address) < 1:
        address = '北京市海淀区彩和坊路海淀西大街74号'
    url = serviceurl + urllib.parse.urlencode(
        {'address':address}
    )+'&'+urllib.parse.urlencode(
        {'key':'DCDBZ-QSZWP-KHIDQ-V7E24-JWFXE-UQBS4'}
    )
    print('Retrieving', url)
    uh = urllib.request.urlopen(url,context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 0:
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    print(json.dumps(js,ensure_ascii=False,indent=4))
    lat = js['result']['location']['lat']
    lng = js['result']['location']['lng']
    print("lat",lat,"lng",lng)

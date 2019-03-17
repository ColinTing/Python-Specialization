import codecs
import sqlite3
import json

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
fhand = codecs.open('where.js','w','utf-8')
#把json的赋值给变量也写进文件中而不只是从json头开始写起
#因为这样where.js中的json数组可方便where.html中for循环调用
fhand.write("myData = [\n")
count = 0
for row in cur:
    #decode()去掉好像也没什么问题，
    #因为在geoload.py文件中插入时用到memoryview()函数，但memoryview()函数返回值不是bytes,所以插入也不是bytes插入，decode()函数就没有必要
    data = row[1].decode()
    try:
        js = json.loads(data)
    except:
        continue
    if not ('status' in js and js['status'] == 'OK'):continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0:continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'","")

    try:
        print(where, lat, lng)
        #count递增放在count判断的上面因为这样在第一条地址信息后就会加上‘,’；如果放到判断后面第二条数据才加上‘,’ 
        # 判断放在正文前的好处是最后一条信息不会加上‘,’
        count = count+1
        if count > 1:
            fhand.write(",\n")
        #因为lat和lng是INTEGER整型，所以转换需要转换成str类型；
        #不然即使where是整形，也写不进js文件中
        output =  "["+str(lat)+","+str(lng)+","+"'"+where+"'"+"]"       
        fhand.write(output)
    except:
        continue
    
#这里在最前面放置换行符是因为最后没有换行符
fhand.write("\n];\n")
#先关闭数据库句柄，再关闭文件句柄
cur.close()
fhand.close()
print(count, "records written to where.js")
print("接下来通过html在地图上展示地址")


        





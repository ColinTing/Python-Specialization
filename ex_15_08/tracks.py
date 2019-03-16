import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur  = conn.cursor()
#创表语句中主键字段缺了INTEGER类型
cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );


    CREATE TABLE Album(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        artist_id INTEGER
    );

    CREATE TABLE Track(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        album_id INTEGER,
        len INTEGER,  rating INTEGER, count INTEGER
    );
''')
def lookup(d,key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None



fname = input('Enter the file:')
if len(fname)<1: fname = 'Library.xml'

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
#缺了dict数量的打印
print("Dict count", len(all))
for entry in all:
    if not lookup(entry, 'Track ID'): continue
    #lookup方法中的key参数填写错了，要首字母大写    
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry,'Album')
    length = lookup(entry,'Total Time')
    rating = lookup(entry,'Rating')
    count = lookup(entry,'Play Count')

    #漏了空值判断
    if name is None or artist is None or album is None:
        continue
    #缺了曲目信息的打印
    print(name, artist, album, length, rating, count)

    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES(?) ',(artist,))

    cur.execute('SELECT id FROM Artist WHERE name = ?',(artist,))
    artist_id = cur.fetchone()[0]
    #title存错了，存成了artist的值
    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES(?,?) ',(album,artist_id))
    #找title又找错了，找成了artist
    cur.execute('SELECT id FROM Album WHERE title = ?',(album,))
    album_id = cur.fetchone()[0]
    #插入的参数多于真实的参数
    cur.execute('INSERT OR REPLACE INTO Track (title,album_id,len,rating,count) VALUES(?,?,?,?,?) ',
    (name,album_id,length,rating,count))

conn.commit()
conn.close()
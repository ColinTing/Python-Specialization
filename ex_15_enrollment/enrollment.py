import json
import sqlite3

conn = sqlite3.connect('enrollmentdb.sqlite')
cur = conn.cursor()

# 表命名不要加复数 “Users” 改成 “User”
#改了建表语句及插入sql中的User，却忘了删除表中的User
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Course (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title    TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id  INTEGER,
    role   INTEGER,
    PRIMARY KEY(user_id, course_id)
);

''')


fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'roster_data.json'

#只需open(file),我却写成了urllib.request.urlopen(url)
#请命名规范些
#data = open(fname).read()
#js = json.loads(data)
#好的命名方法
str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    print(name, title, role)

    cur.execute('''INSERT OR IGNORE INTO User (name) 
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]
    #形式参数又比实际参数多写了一个
    cur.execute('''INSERT OR IGNORE INTO Course (title) 
        VALUES ( ?)''', ( title,) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id,course_id,role) 
        VALUES ( ?, ?, ? )''', ( user_id, course_id, role ) )
    
conn.commit()
conn.close()

import xml.etree.ElementTree as ET

date = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>021</id>
            <name>Colin</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(date)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name:', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attr:', item.get('x'))
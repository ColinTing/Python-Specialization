import xml.etree.ElementTree as ET

date = '''
<person>
    <name>Colin</name>
    <phone type="intl">
        +86 186 6433 1269
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(date)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
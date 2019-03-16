import re

x = 'From: Using the : character zz00'

y = re.findall('^F.+?:',x)
z = re.findall('[0-9a-z]',x)
print(z)
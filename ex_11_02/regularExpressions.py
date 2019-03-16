import re

name = input('Enter a file:')
if len(name)<1:
    name = 'regex_sum_187626.txt'
handle = open(name)
lineStr = ''
for line in handle:
    lineStr = lineStr + ' '+ line.rstrip()

lst = re.findall('[0-9]+',lineStr)
iLst = list()
for sval in lst:
    ival = int(sval)
    iLst.append(ival)


print('Sum:',sum(iLst))

# import re

# name = input('Enter a file:')
# if len(name)<1:
#     name = 'regex_sum_187626.txt'
# handle = open(name)
# print( sum( [ for int(sval) in re.findall('[0-9]+',handle.read()) ] ) )
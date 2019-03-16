rawstr=input('Enter a number:')

try:
    istr = int(rawstr)
except:
    istr = -1

if istr>0:
    print('Nice work')
else:
    print('Not a Number')

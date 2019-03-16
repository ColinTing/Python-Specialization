fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File not exist")
    quit()
lst = list()
lst2 = list()
lineStr = ''
for line in fh:
    lineStr = lineStr + ' '+ line.rstrip()

lst = lineStr.split()
lst.sort() #必须另起一行，因为sort()方法不会返回值

for str in lst:
    if len(lst2) == 0:
        lst2.append(str)
    elif str != lst2[-1]:
            lst2.append(str)

print(lst2)
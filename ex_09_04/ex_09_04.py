fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
for line in fh:
    line = line.rstrip()
    lst = line.split()
    if len(lst)>1 and lst[0] == "From":
        counts[lst[1]] = counts.get(lst[1],0)+1
bigWord = None
bigCount = None
for word, count in counts.items():
    if bigCount is None or bigCount < count:
        bigWord = word
        bigCount = count

print(bigWord, bigCount)
        


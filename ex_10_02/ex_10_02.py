fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
for line in fh:
    line = line.rstrip()
    lst = line.split()
    if len(lst)>5 and lst[0] == "From":
        hour = lst[5].split(':')[0]
        counts[hour] = counts.get(hour,0)+1

for key, val in sorted(counts.items()):
    print(key,val)
#print(sorted([(val,key) for key, val in counts.items()]))
        


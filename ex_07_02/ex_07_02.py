count = 0
s = 0
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("File is not exist")
    quit()
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count = count + 1
    index = line.find(':')
    sval = line[index+1:].rstrip()
    f = float(sval)
    s = s + f
print("Average spam confidence:",float(s/count))
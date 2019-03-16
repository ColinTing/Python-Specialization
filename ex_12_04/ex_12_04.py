import urllib.request, urllib.parse, urllib.error

#用 urllib 创建socket连接

fhanld = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
print(fhanld)
counts = dict()
for line in fhanld:
    words = line.decode().strip().split()
    for word in words:
        counts[word] = counts.get(word,0)+1

print(counts)
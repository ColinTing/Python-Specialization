# name  = input('Enter file:')
# handle = open(name)

# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0)+1

# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count

# print(bigword, bigcount)

name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
    
wordscount  = None
#word = None
for word, count in counts.items():
    # if wordscount is None or count < smallcount:
    #     smallword = word
    #     smallcount = count
    if wordscount is None:
        wordscount = count
    else:
        wordscount += count

print(wordscount)

# Q2. Inverted Index
from collections import defaultdict
sentences = ["the quick brown fox", "jumps over the lazy dog", "the dog barked"]

invertedindex=defaultdict(list)

index=0
for sentence in sentences:
    words=sentence.split()
    for word in words:
        invertedindex[word].append(index)
    index+=1

print(dict(invertedindex))
# Q4. Accumulate Word Lengths
from collections import defaultdict
words = ["hi", "hello", "hey", "bye", "thanks", "ok"]


output=defaultdict(list)
for word in words:
    length=len(word)
    output[length].append(word)
print(dict(output))

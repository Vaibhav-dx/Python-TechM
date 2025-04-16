# Word Frequency Counter
from collections import Counter

with open("story.txt", "r") as file:
    text = file.read().lower()  

words = text.split()
#print(words)
wordfreq = Counter(words)
with open("frequency.txt", "w") as f:
    for word, count in wordfreq.items():
        f.write(f"{word}: {count}\n")


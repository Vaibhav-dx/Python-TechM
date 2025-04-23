def anyalyzetext(text:str):
    words=text.lower().split()
    wordcount=len(words)
    uniquewords=set(words)
    frequency={}
    for word in words:
        frequency[word]=frequency.get(word,0)+1

    return {
        "Total words": wordcount,
        "Unique": len(uniquewords),
        "Frequency":frequency
    }

output=anyalyzetext("vaibhav Dixit vaibhav")
print(output)
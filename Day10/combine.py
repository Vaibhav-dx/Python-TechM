
filenames = ["article.txt", "thought.txt", "story.txt"]

with open("fullbook.txt", "w") as outfile:
    for fname in filenames:
        with open(fname, "r") as infile:
            outfile.write(infile.read() + "\n")



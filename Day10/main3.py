#  Find and Replace "Python" with "PYTHON"
with open("article.txt", "r") as file:
    content = file.read()

word = content.replace("Python", "PYTHON")

with open("article.txt", "w") as file:
    file.write(word)

# Uppercase Writer
with open("input.txt", "r") as input:
    content = input.read()

with open("output.txt", "w") as output:
    output.write(content.upper())

# Student Report
with open("students.txt", "r") as a, open("report.txt", "w") as b:
    for line in a:
        parts = line.strip().split()
        if len(parts) == 3:
            name, age,marks = parts
            status = "Pass" if int(marks) >= 50 else "Fail"
            b.write(f"{name} - {status}\n")

# Reversed
with open("thought.txt", "r") as t:
    lines = t.readlines()

with open("reversed.txt", "w") as r:
    for line in reversed(lines):
        r.write(line)
     
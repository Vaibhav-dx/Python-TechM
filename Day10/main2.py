import os
# 1. Open and Read File (notes.txt) Line-by-Line

try:
    with open("notes.txt", "r",encoding="utf-8") as file:
        for line in file:
            print(line.strip())  
except FileNotFoundError:
    print("File 'notes.txt' not found.")

# 2.Count Lines in a File
try:
    with open("notes.txt", "r",encoding="utf-8") as fl:
        lines = fl.readlines()
        print(f"Total number of lines: {len(lines)}")
except FileNotFoundError:
    print("File 'poem.txt' not found.")


# 3. Write Remainder

tasks = ["Buy clothes", "walking", "assignment", "Exercise", "clg work"]

with open("reminder.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")


# 4. Append to a File
newtask = "Gym"

with open("reminder.txt", "a") as file:
    file.write(newtask + "\n")


# 5. Check If File Exists

if os.path.exists("data.txt"):
    with open("data.txt", "r") as file:
        print(file.read())
else:
    print("File 'data.txt' does not exist.")

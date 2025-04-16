import csv

students = []


try:
    with open("students.txt", "r",newline='') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                name, age, marks = parts
                students.append((name, int(age), int(marks)))
except FileNotFoundError:
    print("File 'students.txt' not found.")
    exit()



def averagemarks():
    totalmarks = sum(marks for _, _, marks in students)
    return totalmarks / len(students) 

average = averagemarks()


with open("top_students.txt", "w") as top:
    top.write("Name Age Marks\n")  
    for name, age, marks in students:
        if marks > average:
            top.write(f"{name} {age} {marks}\n")


with open('students.csv', 'w',newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'Marks'])
    writer.writeheader()
    for name, age, marks in students:
        writer.writerow({'Name': name, 'Age': age, 'Marks': marks})



def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    marks = input("Enter marks: ")

    students.append((name, int(age), int(marks)))
    average = averagemarks()
    print(f"average marks: {average}")

    
    with open('students.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'Marks'])
        writer.writerow({'Name': name, 'Age': age, 'Marks': marks})

def view_students():
    try:
        with open('students.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No records found.")

def main():
    while True:
        print("\n1. Add Student\n2. View Students\n3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        
        
        elif choice == '3':
            break
        

if __name__ == "__main__":
    main()

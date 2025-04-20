# Write a function that takes a list of tuples, each containing (department, employee, salary), and returns a dictionary with departments as keys and a list of (employee, salary) sorted by salary descending.
from collections import defaultdict

def groupemp(data):
    output=defaultdict(list)
    for dept, emp, sal in data:
        output[dept].append((emp,sal))
    return dict(output)



def main():
    data = [
        ('HR', 'Alice', 50000),
        ('HR', 'Bob', 60000),
        ('Tech', 'Charlie', 120000),
        ('Tech', 'Dave', 110000),
        ('Tech', 'Eve', 115000)
    ]   
    grouped=groupemp(data)
    print(grouped)

if __name__=="__main__":
    main()

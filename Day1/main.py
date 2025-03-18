# Assigning values to different variables
x = 42
y = 3.14
z = "Hello"
a = True
b = [1, 2, 3]
c = (4, 5, 6)
d = {"name": "Alice", "age": 25}
e = {10, 20, 30}

# Printing the type of each variable
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'list'>
print(type(c))  # <class 'tuple'>
print(type(d))  # <class 'dict'>
print(type(e))  # <class 'set'>

# Simple Arithmetic Operations
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Simple Comparison Operations
print("Greater:", a > b)
print("Smaller:", a < b)
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater or Equal:", a >= b)
print("Smaller or Equal:", a <= b)

# Simple Logical Operations
x = True
y = False

print("AND:", x and y)
print("OR:", x or y)
print("NOT x:", not x)
print("NOT y:", not y)

# Simple Built-in Function Usage
numbers = [5, 3, 8, 1]

print("Max - Min:", max(numbers) - min(numbers))

# Assign Function to Variable
greet = print
greet("Hello, World!")

# Different Variable Types
a = 10
b = "Python"
c = 3.14

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))

# Type Conversion
num = "123"
converted_num = int(num)

print("Converted Num:", converted_num)
print("Type of Converted Num:", type(converted_num))

# Variable Assignment and Reassignment
x = 5
print("Initial x:", x)

x = "Hello"
print("Reassigned x:", x)

x = 3.14
print("Reassigned x again:", x)

#Order of Operations

result = 2 + 3 * 4 ** 2 / 8
print(result) # 8.0

#Reassignment
count = 10
print(count) # 10
count = 20
print(count)    # 20

score = 100
score += 10
print(score) # 110
score -= 5
print(score) # 105
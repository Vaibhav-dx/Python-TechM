#1
# syntax error- missing ":"
for i in range(5)
    print(i)
# correct code
for i in range(5):
    print(i)

# Arithmetic Error-Division by Zero error
x = 10 / 0
# correct code
x=10/2


# Logical error- wrong formula
def calculate_area(radius):
    return 2 * 3.14 * radius
# correct code
def calculate_area(radius):
    return 3.14 * radius ** 2

# 2
def process_data(data):
    total = 0
    for item in data:
        # error occur if item in not a num
        total += int(item) 
    return total / len(data)

print(process_data(['10', '20', 'abc', '30']))

# correct code
def process_data(data):
    total = 0
    count = 0

    for item in data:
        try:
            total += int(item)  #Convert only valid numbers
            count += 1
        except ValueError:
            print(f"Skipping invalid value: {item}")  # Ignore non-numeric values

    return total / count if count > 0 else 0  #Prevent division by zero

print(process_data(['10', '20', 'abc', '30']))

# 3.Advanced Debugging Challenge
import random

def unreliable_function():
    number = random.choice([0, 1, 2])
    # divisionbyzero error can occur if choosen number is 0
    return 10 / number

for i in range(10):
    print(unreliable_function())
# correct code
import random

def unreliable_function():
    number = random.choice([0, 1, 2])
    try:
        return 10 / number  
    except ZeroDivisionError:
        return "Error: Division by zero"

for i in range(10):
    print(unreliable_function())

# 4.Writing Debug-Friendly Code
def calculate_discount(price, discount):
    return price - (price * discount / 100)

print(calculate_discount(100, '10%'))


# 5. Rubber Duck Debugging
numbers = [1, 2, 3, 4, 5]
result = 1
for num in numbers:
    result *= num
print("Product:", result)

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]  

# Initialize the result variable with 1 (since 1 is the identity for multiplication)
result = 1  

# Loop through each number in the list
for num in numbers:
    # Multiply the current number with the result and update the result variable
    result *= num  # Equivalent to result = result * num

# Print the final product of all numbers in the list
print("Product:", result)  # Output: Product: 120



# 6.Advanced Challenge: Debug a Multi-threaded Program
# Race Condition- Multiple threads try to access and modify a shared resources at the same time, leads to incorrect expected output.
import threading

counter = 0
def increment():
    global counter
    for _ in range(100000):
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Counter:", counter)  # Expected: 200000

# correct code-using thread lock
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  # Only one thread can enter at a time
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Counter:", counter)  # Correct: 200000

# 7.Activity: Debug with Breakpoints
def divide(a, b):
    result = a / b #zero division error
    return result

a = 10
b = 0
print(divide(a, b))

# correct code
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

a = 10
b = 0
print(divide(a, b))  # Output: Error: Cannot divide by zero!


# 8.Memory Leaks and Performance Debugging
# Problems-1.Stores large data in memory 2.Delay-time.sleep
import time

def inefficient_function():
    result = []
    for i in range(100000):
        result.append(i * 2) 
    time.sleep(2)  
    return result

print(len(inefficient_function()))

# correct code
def efficient_function():
    return [i * 2 for i in range(100000)]  # List comprehension 
print(len(efficient_function()))

# 9. Unexpected None
def add(a, b):
    result = a + b
print(add(3, 4))
# function return none beacuse it calculates the result but does not return

def add(a, b):
    result = a + b
    return result  # Returning the result

print(add(3, 4))


# 10. Silent Failures
try:
    result = 10 / 0
except:
    pass
print("No error detected!")
#  10 / 0 raises ZeroDivisionError.
# The except block catches the error but does nothing (pass).
# The program continues execution without informing about the error.
# This results in a silent failure.

# Correct code
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")


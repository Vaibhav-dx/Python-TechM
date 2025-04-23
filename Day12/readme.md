
# 1. Returning vs Printing

def add_and_print(a, b):
    print(a + b)

result = add_and_print(3, 4)
print("Returned:", result)
7
Returned: None
- The value is printed inside the function.
- Nothing is returned.

def add_and_return(a, b):
    return a + b

result = add_and_return(3, 4)
print("Returned:", result)

- Value is returned and can be stored or reused.

# 2. Mutable Object Side-Effect

def append_value(lst):
    lst.append(100)

nums = [1, 2, 3]
append_value(nums)
print(nums)  # Output: [1, 2, 3, 100]
Lists are mutable. Changes inside the function affect the original object.

## 3. Global Variable and Risk
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1
**Risks of using global:**
- Harder to trace where a variable changed.
- Breaks modularity.
- May cause bugs in larger programs.

## 4. Function Composition: Compute `sqrt(x^2 + y^2)`
import math

def square(n):
    return n * n

def add(a, b):
    return a + b

def calculate_hypotenuse(x, y):
    return math.sqrt(add(square(x), square(y)))

print(calculate_hypotenuse(3, 4))  # Output: 5.0
- Small helper functions combine to perform a larger task.

## 5. Local Scope Bug and Fix

### Buggy Code:

def set_value():
    value = 10

set_value()
print(value)  # NameError: value is not defined

### Fixed Code:
def set_value():
    return 10

value = set_value()
print(value)  # Output: 10

- The original code failed because `value` was local to the function.
- Returning and assigning the value outside solves the scope issue.



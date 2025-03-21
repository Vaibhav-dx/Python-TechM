# Q1.Circular Import
# module_a.py imports module_b.py.
# module_b.py imports module_a.py.
# This infinite loop leads to an ImportError or AttributeError.
# modul_a.py
def func_a():
    return "Function A"

def call_func_b():
    from module_b import func_b  #Import inside function to avoid circular import
    return func_b()

print(call_func_b())
# module_b.py
def func_b():
    return "Function B"


# Q2.Dynamic Module Loading
import importlib

# Get user input
module_name = input("Enter module name: ")  
function_name = input("Enter function name: ")  
argument = input("Enter argument: ")  

try:
    # Dynamically import the module
    module = importlib.import_module(module_name)

    # Get the function from the module
    func = getattr(module, function_name)

    argument = float(argument)

    # Execute the function and print result
    result = func(argument)
    print("Output:", result)

except ModuleNotFoundError:
    print("Error: Module not found!")
except AttributeError:
    print("Error: Function not found in module!")
except ValueError:
    print("Error: Invalid argument!")
except Exception as e:
    print(f"Unexpected error: {e}")

# Q3. Custom Module with Exception Handling
#calculator.py
# calculator.py

def divide(a, b):
    try:
        return a / b  # Division operation
    except ZeroDivisionError:
        return "Cannot divide by zero."  #division by zero error
    except Exception as e:
        return f"Error: {e}"  #other unexpected errors
# main.py
import calculator  # Import the custom module

print(calculator.divide(10, 2))  # 5.0
print(calculator.divide(10, 0))  # Cannot divide by zero.
print(calculator.divide("10", 2))  # Output: Error: unsupported operand type(s)


# Q4. Advanced Import Strategies
# advanced_import.py

def execute_function(module_name, function_name, *args):
    module = importlib.import_module(module_name) #import the specified module dynamically.
    if hasattr(module, function_name): # checks if the function exists in the imported module.
        function = getattr(module, function_name)
        return function(*args)
    else:
        return "Function not found."

print(execute_function("math", "sqrt", 16))  # 4.0


# Q5.Measuring Import Time
# Single Import
import time

start = time.time()
import math
end = time.time()

print(f"Single import time: {end - start:.6f} seconds")

# Multiple Imports
import time

start = time.time()
import math
import random
import os
import sys
end = time.time()

print(f"Multiple imports time: {end - start:.6f} seconds")

#Q7.Investigate sys.path
import sys
print(sys.path)
# To add custom path
import sys

# Add a custom directory
sys.path.append('/custom/path/to/modules')

# Now you can import your module from that path
import mymodule  

print(mymodule.some_function()) 

# Q8. Mocking Modules for Testing
from unittest import mock
import math  # Import the actual module

# Mocking math.sqrt to always return 100
with mock.patch('math.sqrt', return_value=100):
    print(math.sqrt(25))  # 100

# Outside the mock context, it works normally
print(math.sqrt(25))  #  5.0

# Q9. Import Side Effects
# Create a Module (my_module.py)
print("This runs on import!")

def my_function():
    return "Hello from my_function!"
# import module in (main.py)
import my_module

print("Import is done!")
print(my_module.my_function()) 

# Q10.Investigate Python’s Import Caching
# mymodule.py
print("Module mymodule is being imported!")

def hello():
    return "Hello from mymodule!"
# main.py
import sys
import mymodule  #First import

print(sys.modules['mymodule'])  #if mymodule is in cache

import mymodule  # Second import
print("Re-imported mymodule!")
# Errors in Python can be broadly categorized into three types:

1.Syntax Errors- These occur when the Python interpreter finds incorrect syntax in the code.The program won’t run until the syntax error is fixed.

2.Runtime Errors (Exceptions)-These errors occur while the program is running.Even if the syntax is correct, unexpected conditions (like dividing by zero or accessing an invalid index) cause exceptions.

3.Logical Errors- These are errors in the logic of the program.The code runs without crashing but produces incorrect results.
These are hardest to detect because Python doesn’t give an error


# Debugging Complex Functions
  - ValueError: The function tries to convert the string 'abc' to an integer, which will cause an error.
  - SyntaxError: The print statement is missing a closing parenthesis.
  - Potential ZeroDivisionError: If data is an empty list, len(data) would be 0, leading to a division by zero.

# Advanced Debugging Challenge
  - The function randomly selects a number from [0, 1, 2], but if 0 is chosen, a ZeroDivisionError occurs because 10 / 0 is undefined.

# Writing Debug-Friendly Code
  -  issue in code is that '10%' is a string, not a number. The function expects discount to be an integer or float, but it is given a string ('10%'), causing a TypeError when performing arithmetic operations.

# Rubber Duck Debugging
 ## Creating a List
  - numbers = [1, 2, 3, 4, 5]
  - We create a list called numbers that contains five values: [1, 2, 3, 4, 5].
  - A list is a collection of items that are stored in square brackets ([]).
 ## Initializing a Variable
  - result = 1
  - We create a variable named result and set its value to 1.
  - This variable will be used to store the product of all numbers in the list. 
 ## Looping Through the List
  - for num in numbers:
  - result *= num
  - This is a for loop that goes through each number in the numbers list one by one.
  - num represents the current number from the list during each loop cycle.
  - result *= num is shorthand for:
  - result = result * num
  - which means we multiply result by num and update result.
 ## Understanding the Loop Execution
 ## Printing the Final Result
   - print("Product:", result)
   - The print() function displays the final product of the numbers in the list.
   - Product: 120
# Silent Failures
  - The code does not raise an error because the try-except block catches the exception and handles it using the pass statement. 
  - Normally, dividing by zero (10 / 0) would raise a ZeroDivisionError, but since the except block is present without specifying 
  - an exception type, it catches all exceptions silently. The pass statement means "do nothing," so the program continues execution 
  - without interruption. As a result, the print("No error detected!") statement runs normally, even though an error occurred inside the try block.
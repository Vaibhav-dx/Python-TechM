# Print a welcome message three times
def welcome():
    print("Welcome to Python!")

welcome()
welcome()
welcome()

# Return the square of a number
def square(n):
    return n * n
print(square(5))  

# Return True if number is even
def is_even(num):
    return num % 2 == 0
print(is_even(4))  # Output: True
print(is_even(5))  # Output: False


# Return full name
def full_name(first, last):
    return first + " " + last
print(full_name("Vaibhav", "Dixit")) 

# Return area of circle using
def circle_area(radius):
    pi = 3.14
    return pi * radius * radius
print(circle_area(3))


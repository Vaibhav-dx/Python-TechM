# Iteration
Iteration is the process of repeatedly executing a set of instructions. In Python, iteration is commonly performed using loops.

# Working of for-loop
1.Initialize the loop variable with the first item in the sequence.
2.Execute the loop body.
3.Move to the next item and repeat until the sequence is completed.

# For Loop Basics
Write a for loop to print numbers from 1 to 10.

# Code:
python
for i in range(1, 11):
    print(i)

# Explanation:
- `range(1, 11)` generates numbers from 1 to 10.
- `for i in range(...)` iterates through each number and prints it.


# Example with a List:
python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Working with Strings and Loops
- **Strings** are iterable, so you can loop through characters:
python
word = "Python"
for char in word:
    print(char)


# . String Iteration: Count Vowels in a String
Write a program that counts the number of vowels in a given string.

# Code:

string = "Hello, World!"
vowels = "aeiouAEIOU"
count = sum(1 for char in string if char in vowels)
print("Number of vowels:", count)

# Explanation:
- The program iterates through the string.
- It checks each character if it's a vowel (both uppercase and lowercase).
- The `sum()` function accumulates the count of vowels.

---

# 3. Accumulator Pattern: Sum of Squares from 1 to 100
Calculate the sum of squares from 1 to 100.

# Code:

sum_of_squares = sum(i**2 for i in range(1, 101))
print("Sum of squares:", sum_of_squares)

# Explanation:
i**2` calculates the square of each number.
sum()` accumulates the total sum.



# 4. Nested Loops: Multiplication Table (10x10)
Generate a multiplication table up to 10x10.

# Code:

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:3}", end=" ")
    print()

# Explanation:
Outer loop iterates over rows (1 to 10).
Inner loop iterates over columns (1 to 10), calculating `i * j`.
- The `print()` function formats the table with spacing.



# 5. Image Processing: Invert Colors Using PIL
Use the PIL (Pillow) library to invert colors of an image.

# Code:

from PIL import Image, ImageOps
img = Image.open("example.jpg")
inverted_img = ImageOps.invert(img.convert("RGB"))
inverted_img.show()

# Explanation:
- `Image.open("example.jpg")` loads the image.
- `ImageOps.invert()` inverts the image colors.
- `.show()` displays the processed image.









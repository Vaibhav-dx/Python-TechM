# 1. **For Loop Basics:** Write a for loop to print numbers from 1 to 10.
for num in range(1, 11):
    print(num)

# 2. **String Iteration:** Write a program that counts vowels in a string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

string = "Hello World"
print("Number of vowels:", count_vowels(string))


# 3. **Accumulator Pattern:** Calculate the sum of squares from 1 to 100.
sum_of_squares = sum(num**2 for num in range(1, 101))
print("Sum of squares:", sum_of_squares)


# 4. **Nested Loops:** Create a multiplication table up to 10x10.
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end=" ")  # Format spacing
    print()


# 5. **Image Processing:** Use PIL to invert the colors of an image
from PIL import Image, ImageOps

img = Image.open("example.jpg")  # Load image
inverted_img = ImageOps.invert(img.convert("RGB"))  # Invert colors
inverted_img.show()  # Show the inverted image

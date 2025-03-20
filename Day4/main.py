# 4.Write code to access the last character of a string.
text = "Python"
last_char = text[-1]  # Accessing the last character, since python allows negative indexing
print(last_char)  


# 5.Create a list of numbers and access the third element.
numbers = [10, 20, 30, 40, 50]
third_element = numbers[2]  # Index 2 refers to the third element, since indexing starts from 0
print(third_element)  # Output: 30

# 8.How would you reverse a string using slicing?
text = "Python"
reversed = text[::-1]  # Slicing with step -1 reverses the string
print(reversed)  # Output: "nohtyP"

# 9.Demonstrate list concatenation and repetition with examples.
# List Concatenation (+ Operator)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2  
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# List Repetition (* Operator)
numbers = [10, 20]
repeated_list = numbers * 2  
print(repeated_list)  # Output: [10, 20, 10, 20]

# 10.Write code to count the occurrences of an element in a list.
my_list = [1, 2, 2, 3]
print(my_list.count(2))  # Output: 2

# 13.Write code to split the sentence: "Learn Python, step by step!" into words.
sentence = "Learn Python, step by step!"
words = sentence.split()  # ['Learn', 'Python', 'step', 'by', 'step']


# 14. Join a list ['Python', 'is', 'fun'] into a single string.
words=['Python', 'is', 'fun'] 
sentence=' '.join(words) #python is fun

# 15.Given a list numbers = [1, 2, 2, 3, 4, 2], find the index of the first 2.
numbers = [1, 2, 2, 3, 4, 2]
index = numbers.index(2)
print(index) #output 1

# 16. String Palindrome
def ispalindrome(s):
    return s == s[::-1]  # Compare string with its reverse
string = "naman"
print(ispalindrome(string))  # Output: True

string = "hello"
print(ispalindrome(string))  # Output: False

# 17.Implement a function that returns the length of the longest word in a sentence.

# Python program to find the number of characters 
# in the longest word in the sentence. 

def longestWordLength(string): 
    length = 0
    # Finding longest word in sentence
    for word in string.split():
        if(len(word) > length):
            length = len(word)  
    return length 
string = "I am an intern at Tech Mahindra"
print(longestWordLength(string))

# 18.Demonstrate nested list indexing.
# A nested list is a list within another list.
# Nested list (list inside a list)
matrix = [
    [11, 42, 3], 
    [24, 5, 60], 
    [170, 30, 90]
]

# Accessing elements
print(matrix[0][1])  # 42 (First row, second element)
print(matrix[2][2])  # 5 (Third row, third element)
print(matrix[1])     # [11,42,3] (Second row)

# 19. How do you convert a list of characters into a string?
words=['v','a','i','b','h','a','v']
string=' '.join(words)
print(string)

# 20.Write code to remove duplicates from a list while preserving order.

def remove_duplicates(lst):
    seen = set()
    return [seen.add(item) or item for item in lst if item not in seen]

numbers = [1, 2, 2, 3, 4, 3, 5, 1]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4, 5]

# 21.Write a function that takes a list of tuples and sorts it by the second element of each tuple.
def sort(lst):
    return sorted(lst, key=lambda x: x[1])
tuples_list = [(1, 3), (2, 1), (4, 2), (3, 5)]
sorted_list = sort(tuples_list)
print(sorted_list)  # Output: [(2, 1), (4, 2), (1, 3), (3, 5)]


# 22.Implement a program to flatten a nested list of arbitrary depth.
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

print(flatten([1, [2, [3, 4], 5], 6]))  # Output: [1, 2, 3, 4, 5, 6]

# 23.Create a function that rotates a list to the right by k steps.
def rotate_list(nums, k):
    k = k % len(nums)  # Handle cases where k > len(nums)
    return nums[-k:] + nums[:-k]  # Slice and concatenate

nums = [1, 2, 3, 4, 5]
k = 2
print(rotate_list(nums, k))  # Output: [4, 5, 1, 2, 3]

# 24.Given two strings, write a function that returns True if they are anagrams.
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)  # Sort both strings and compare

print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False

# 26.Implement a function that merges two sorted lists into one sorted list.
def merge_sorted_lists(list1, list2):
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:]) #adding remaining element
    merged.extend(list2[j:])
    
    return merged
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(merge_sorted_lists(list1, list2))  
# Output: [1, 2, 3, 4, 5, 6, 7, 8]

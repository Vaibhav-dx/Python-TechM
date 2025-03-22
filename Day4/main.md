# 1.Define a sequence. What types of sequences exist in Python?
In Python, a sequence is an ordered collection of items. The order of elements is preserved, and each element is accessible via its index. The main types of sequences in Python are:

Strings
Lists
Tuple

# 2.How are strings, lists, and tuples different from each other?
# String-
 A string is a sequence of characters and is immutable, meaning it cannot be changed after creation. Since strings are immutable, modifying a character like s[0] = 'J' will result in an error.

# List- 
A list is a collection of elements (numbers, strings, or even other lists) and is mutable, meaning elements can be modified. It is defined using square brackets ([1, 2, 3]). Lists use more memory but allow modifications like l[0] = 10.

# Tuple-
A tuple is similar to a list but immutable, meaning its elements cannot be changed after creation. It is defined using parentheses ((1, 2, 3)). Tuples are more memory-efficient and faster than lists but cannot be modified.

# 3. Explain how indexing works in Python with an example.
Indexing in Python is used to access individual elements in sequences like strings, lists, and tuples. Python supports zero-based indexing. It also supports negative indexing, where -1 refers to the last element, -2 refers to the second-last, etc.
# Example:
numbers = [10, 20, 30, 40, 50]

# Positive Indexing
print(numbers[0])   # Output: 10 (First element)
print(numbers[3])   # Output: 40 (Fourth element)

# Negative Indexing
print(numbers[-1])  # Output: 50 (Last element)
print(numbers[-3])  # Output: 30 (Third-last element)

# 6.What is the result of len([1, [2, 3], 4]) and why?
len() function counts the number of elements at top level.
Output will be 3 elements because, it counts 1 as single integer, [2,3] count them as single element and 4 as single element.

# 7. Explain slicing with a practical example.
Slicing allows to extract a portion of a sequence(like a string, list, or tuple).
syntax: sequnce[start:stop:step]
# Example
numbers = [10, 20, 30, 40, 50, 60]

# Extract elements from index 1 to 4 (excluding index 4)
subset = numbers[1:4]  
print(subset)  # Output: [20, 30, 40]

# 11. What will my_tuple = (1, 2, 3); print(my_tuple[1:]) output?
Output-(2, 3), because it uses slicing to extract elements starting from index 1 (inclusive) to the end.

# 12.Explain the difference between list.append() and list.extend().
The append() method in Python adds an entire element as a single item to the end of a list, meaning if you append a list, it will be nested within the original list. For example, numbers = [1, 2, 3]; numbers.append([4, 5]) results in [1, 2, 3, [4, 5]]. 
Extend() adds elements from an iterable individually to the list. So, numbers.extend([4, 5]) results in [1, 2, 3, 4, 5]. The key difference is that append() increases the list length by one, while extend() expands it based on the number of elements in the iterable.





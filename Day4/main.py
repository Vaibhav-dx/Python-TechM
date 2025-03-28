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



# # Assignement-2
#Q1.Task: Identify the longest pipeline and return pipelines taking more than a given threshold time.

def func(pipelines,threshold):
    longest=max(pipelines,key=lambda x:x[1])

    exceeding=[p for p in pipelines if p[1]>threshold]
    return longest,exceeding

pipelines = [
    ("Data Ingestion", 30),
    ("Preprocessing", 45),
    ("Model Training", 120),
    ("Evaluation", 20)
]
threshold = 40

longest, exceeding = func(pipelines, threshold)

# Output results
print("Longest Pipeline:", longest)
print("Pipelines Exceeding Threshold:", exceeding)


#Q2. Extract unique error codes
logs = """ERROR 404: Not Found
INFO: Connection established
ERROR 500: Internal Server Error
ERROR 404: Not Found
"""
error_codes = {line.split()[1] for line in logs.split("\n") if line.startswith("ERROR")}#logs.split("\n")-splits logs into seprate lines
# line.startswith("ERROR")-checking condition
# line.split()[1] again splitting, and acessing second element

print(error_codes)  # Output: {'404', '500'}

# Q3.Task: Parse key-value pairs from a configuration string.
# Input:
config = "host=127.0.0.1;port=8080;mode=debug"

# Split the string and create a list of tuples
config_tuples = [tuple(pair.split("=")) for pair in config.split(";")]
# splitting by ;
# tuple(pair.split("=")) again splitting by "=" and converting to tuple
print(config_tuples)


# Q4.Task: Extract unique hashtags from a social media post.
post = "Loving the new #Python course! #Coding #Python #Learning"

# Split the post into words
words = post.split()

# Extract unique hashtags
hashtags = {x for x in words if x.startswith("#")}

print(hashtags)  # Output: {'#Python', '#Coding', '#Learning'}

# Q5.Extract every third character from a string.
secret_message = "hweollrolwd"
decoded_message = ""

for i in range(0, len(secret_message), 2):  
    decoded_message += secret_message[i]

print(decoded_message)  

# Q6.Find the product with the highest quantity.
inventory = [
    ("Apples", 50),
    ("Oranges", 75),
    ("Bananas", 30)
]
largest=max(inventory,key=lambda x:x[1])
print(largest)

# Q7.Extract scores from a survey string and find min/max.
survey_data = "5,3,4,1,2"

# Convert each string number to an integer using list comprehension
scores = [int(x) for x in survey_data.split(",")]

# Find max and min values
maxscore = max(scores)
minscore = min(scores)

print(f"Max Score: {maxscore}, Min Score: {minscore}")

#Q8.# Define users and roles
users = ["Alice", "Bob", "Charlie"]
roles = ("Admin", "Editor", "Viewer")

# Create a dictionary mapping users to roles
access_control = dict(zip(users, roles))

# Print user roles
for user, role in access_control.items():
    print(f"{user}: {role}")


# Q9.Categorize tickets based on message length.
def categorize_message(message):
    length = len(message)
    
    if length < 20:
        category = "Short"
    elif 20 <= length <= 50:
        category = "Medium"
    else:
        category = "Long"
    
    return f"Category: {category}"

message = "My account is locked, please help!"
print(categorize_message(message))  # Output: Category: Medium

# Q10.
products = ["Laptop", "Smartphone", "Wireless Headphones"]
longest = max(products, key=len)  # Finds the longest product name
print(longest)  # Output: 'Wireless Headphones'


# Q11.Task: Extract the last 10 sensor readings and calculate the average.
# # Input:
sensor_readings = [12, 15, 14, 16, 20, 22, 21, 23, 25, 30, 28, 27]
last_10=[]
for i in range(len(sensor_readings)-1, 1, -1):
    last_10.append(sensor_readings[i])
print(last_10)
average = sum(last_10) / len(last_10)
print("Average:", average) #output=22

# Q12.# Task: Reverse the list of transactions.
# Input:
transactions = [100, -50, 200, -150, 50]
reverse=[]
for i in range(len(transactions)-1,-1,-1):
    reverse.append(transactions[i])
print(reverse)
# [50, -150, 200, -50, 100]

# Alternate
transactions = [100, -50, 200, -150, 50]
reverse = transactions[::-1]  # Reverse using slicing
print(reverse)

# Q13.Task: Format logs with timestamps.
logs = ["System Boot", "Network Connected", "User Login"]
timestamp = "2025-03-20"
formatted_logs = [f"{timestamp}: {log}" for log in logs]

print(formatted_logs)

# Q14.Task: Generate patterns with repetition.
# Input:
symbol = "*"
pattern=(symbol+" ")*5
print(pattern)

# Q15.Count keyword occurrences.
feedback = "The product is excellent, absolutely excellent!"
keyword = "excellent"

count = feedback.lower().count(keyword)  # Convert to lowercase for case insensitivity

print(f"'{keyword}' count: {count}")

# Q16.Task: Find the index of the first occurrence of "error".
log = "INFO: All systems go. ERROR: Failed to start service."
keyword = "ERROR"
index = log.find(keyword)  # Find the first occurrence
print(f"Index: {index}")


# Q17.Task: Parse CSV data into lists.
csv_data = "Alice,25,Engineer\nBob,30,Doctor\nCharlie,22,Artist"
# First, split by new lines, then split each row by commas
new_csv = [row.split(",") for row in csv_data.split("\n")]

print(new_csv)

# Q18.Task: Generate usernames from full names.
names = ["Alice Wonderland", "Bob Builder", "Charlie Chaplin"]
# Extract first letter of first name + last name
usernames = [f"{name.split()[0][0]}{name.split()[1]}" for name in names]
print(usernames)



# Q19.Task: Count messages per user from chat logs.
chat_logs = [
    "Alice: Hi!",
    "Bob: Hello!",
    "Alice: How are you?",
    "Bob: I’m good, thanks!"
]

# Dictionary to store message counts
message_count = {}
for log in chat_logs:
    user = log.split(":")[0]  # Extract username before ':'
    if user in message_count:
        message_count[user] += 1  # Increment count if user exists
    else:
        message_count[user] = 1  # Initialize count if user is new
for user, count in message_count.items():
    print(f"{user}: {count} messages")


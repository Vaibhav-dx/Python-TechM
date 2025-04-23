# Sum of all even numbers in a list
def evensum(number:list[int])->int:
    total=0
    for num in number:
        if num%2==0:
            total+=num
    return total
print(evensum([2,3,4,5,6,7,8]))

# Reverse String
def reverse(s:str)->str:
    return s[::-1]
print(reverse("vaibhav"))

# count vowels
def countvowels(sentence:str)->int:
    vowels="aeiouAEIOU"
    return sum(1 for char in sentence if char in vowels)
print(countvowels("vaibhav dixit"))


# Avergae Marks
def avg(marks:list[float])->float:
    if not marks:
        return 0.0
    return sum(marks)/len(marks)
print(avg([80,70,90,85]))
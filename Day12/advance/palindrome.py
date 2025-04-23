def ispalindrome(s:str)->bool:
    s=s.replace(" ","").lower()
    return s==s[::-1]

print(ispalindrome("Naman Naman"))

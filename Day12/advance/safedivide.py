def safedivide(x:float,y:float)->float:
    try:
        return x/y
    except ZeroDivisionError:
        return "can not divide by zero"
    
print(safedivide(10,2))
print(safedivide(10,0))
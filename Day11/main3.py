# Q3. Deep Copy Trap
import copy
original={
    'name':'Vaibhav',
    'scores': [90,85,88]
}
shcopy=original.copy()
shcopy["scores"].append(100)
print(original)
print(shcopy)
# here changes are done in both original and copy because, both share the same scores list.

# Deepcopy
original={
    'name':'Vaibhav',
    'scores': [90,85,88]
}
dpcopy=copy.deepcopy(original)
dpcopy["scores"].append(100)
print(original)
print(dpcopy)
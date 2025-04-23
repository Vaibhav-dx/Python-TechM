def flattenlist(l:list)->list:
    flat=[]
    for item in l:
        if isinstance(item,list):
            flat.extend(flattenlist(item))  
        else:
            flat.append(item)
    return flat

print(flattenlist([1, [2, [3, 4], 5], 6]))  
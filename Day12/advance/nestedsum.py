def nestedsum(data:list)->int:
    total=0
    for item in data:
        if isinstance(item,list):
            total+=nestedsum(item)

        else:
            total+=item

    return total
print(nestedsum([[1, 2], [3, [4, 5]], 6]))
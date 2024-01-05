def count_list(list):
    count = 0
    if len(list) == 0:
        return 0
    else:
        return 1 + count_list(list[1:])
    
listA = [1, 2, 3]
print(count_list(listA))
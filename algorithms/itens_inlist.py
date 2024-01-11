def count_list(list):
    if len(list) == 0:
        return 0
    else:
        return 1 + count_list(list[1:])
    
list_a = [1, 2, 3]
print(count_list(list_a))
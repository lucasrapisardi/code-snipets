def binary_search(list, value):
    low = 0
    high = len(list) - 1
    middle = len(list) // 2
    
    while low <= high:
        guess = list[middle]
        if guess == value:
            return middle
        if guess > value:
            high = middle - 1
        else:
            low = middle + 1
    return None

num = [1, 2, 3, 4, 5]
print(binary_search(num, 3))

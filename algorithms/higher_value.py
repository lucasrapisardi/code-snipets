def higher_value(list):
    if len(list) == 0:
        return 0
    else:
        higher = list[0]
        if list[1:] > higher:
            higher = higher_value(list)
    return higher

list_a = [5, 3, 9]
print(higher_value(list_a))
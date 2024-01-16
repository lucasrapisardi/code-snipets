def max_key(my_dictionary):
    max_value = 0
    max_key = 0
    for key, value in my_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key

print(max_key({1:100, 2:100, 3:100, 4:100}))
print(max_key({"a":100, "b":10, "c":1000}))
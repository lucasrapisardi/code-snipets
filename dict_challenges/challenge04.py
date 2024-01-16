def values_that_are_keys(my_dictionary):
    values_keys = []
    for key in my_dictionary.keys():
        if key in my_dictionary.values():
            values_keys.append(key)
    return values_keys

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))

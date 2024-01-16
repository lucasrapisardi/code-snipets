from line_profiler import profile

"""kernprof -l -v codecademy/dict_challenges/challenge02.py to test performance"""
@profile
def sum_even_keys(my_dictionary):
    values = 0
    for key, value in my_dictionary.items():
        if (key % 2 == 0):
            values += value
    return values

@profile
def sum_even_keys2(my_dictionary):
    values = 0
    for key in my_dictionary.keys():
        if (key % 2 == 0):
            values += my_dictionary[key]
    return values

print(sum_even_keys({1:5, 2:2, 3:3}))
print(sum_even_keys({10:1, 100:2, 1000:3}))

print(sum_even_keys2({1:5, 2:2, 3:3}))
print(sum_even_keys2({10:1, 100:2, 1000:3}))
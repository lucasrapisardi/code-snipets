def sum_values (my_dictionary):
    values = 0
    for value in my_dictionary.values():
        values += value
    return values

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
print(sum_values({10:1, 100:2, 1000:3}))
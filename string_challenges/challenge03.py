

def count_multi_char_x  (word, multi_char_x):
    # return word.count(multi_char_x)
    splits = word.split(multi_char_x)
    return len(splits) - 1
    

print(count_multi_char_x("mississippi", "iss"))
print(count_multi_char_x("apple", "pp"))
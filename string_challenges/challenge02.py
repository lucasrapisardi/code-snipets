

def count_char_x (word, char_x):
    # return word.count(char_x)
    count = 0
    for letter in word:
        if letter == char_x:
            count += 1
    return count
    

print(count_char_x("mississippi", "m"))

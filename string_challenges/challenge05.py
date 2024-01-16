def x_length_words(sentence, x):
    split = sentence.split()
    for slice in split:
        if len(slice) < x:
            return False
    return True

print(x_length_words("i i vai virar", 2))
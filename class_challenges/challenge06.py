"""As palavras de input serão as chaves, enquanto que seus valores serão o comprimento de sua respectiva palavra"""
def word_length_dictionary(words):
    word_length_dict = { word: len(word) for word in words }
    return word_length_dict

print(word_length_dictionary(["apple", "dog", "cat"]))
print(word_length_dictionary(["a", ""]))
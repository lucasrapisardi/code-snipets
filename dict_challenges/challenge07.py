"""As chaves serão as palavras e seus valores serão a frequência que as chaves aparecem"""
@profile
def frequency_dictionary(words):
    frequency_dict = { word : words.count(word) for word in words }
    return frequency_dict

print(frequency_dictionary(["apple", "apple", "cat", 1]))
print(frequency_dictionary([0,0,0,0,0]))
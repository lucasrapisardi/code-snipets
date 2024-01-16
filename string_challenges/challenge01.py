letters = "mississippi"

# def unique_english_letters(word):
#     differetent_letter = []
#     letters = 0
#     for letter in word:
#         if letter not in differetent_letter:
#             differetent_letter.append(letter)
#     for l in differetent_letter:
#         letters += 1
#     return letters

def unique_english_letters(word):
    unique = 0
    for letter in word:
        if l in letter:
            unique += 1

print(unique_english_letters(letters))
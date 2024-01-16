# How to set up two pointers in an array
def two_pointers(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        if array[left] != array[right]:
            return False
        else:
            left = left + 1
            right = right -1
    return True

def is_palindrome(s):
    return two_pointers(s)

print(is_palindrome("kayak"))
print(is_palindrome("hello"))
print(is_palindrome("RACEACAR"))
print(is_palindrome("A"))
print(is_palindrome("ABCDABCD"))

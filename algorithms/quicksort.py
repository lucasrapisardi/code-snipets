def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        anchor = arr[0]
        smaller = [ i for i in arr[1:] if i < anchor ]
        higher = [ i for i in arr[1:] if i > anchor ]
        return quicksort(smaller) + [anchor] + quicksort(higher)
    

print(quicksort([10, 5, 2, 1, -4, -2, 900, 50/2, 13, 25]))
print(quicksort([]))
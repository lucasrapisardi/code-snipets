def search_smallest(arr):
    small = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < small:
            small = arr[i]
            smallest_index = i 
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        small = search_smallest(arr)
        new_arr.append(arr.pop(small))
    return new_arr

arr = [6,1,5,7,9,2,3,21,50,-3,19]
print(selection_sort(arr))
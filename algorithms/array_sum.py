def array_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + array_sum(arr[1:])

arr = [1,3]
print(array_sum(arr))
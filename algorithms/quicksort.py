def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivo = arr[0]
        menores = [ i for i in arr[1:] if i < pivo ]
        maiores = [ i for i in arr[1:] if i > pivo ]
        return quicksort(menores) + [pivo] + quicksort(maiores)
    

print(quicksort([10, 5, 2, 1, -4, -2, 900, 50/2, 13, 25]))

flow_ids = ["a89f3f91-0004-4f6d-9dc2-774f9e3c0afb",
"44d7db82-f054-4358-82ed-e21742d686d6"]
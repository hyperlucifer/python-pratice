def miss(n, arr):
    l = arr[n-1]
    s = arr[0]
    las = [*range(s, l+1)]
    i = j = 0
    while i < len(las) and j < len(arr):
        if las[i] != arr[j]:
            print(las[i])
            return
        i += 1
        j += 1
    if i < len(las):  # if still some elements left in las
        print(las[i])

arr = [1, 2, 5]
miss(len(arr), arr)

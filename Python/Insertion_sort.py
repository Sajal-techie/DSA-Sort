def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        pos = i
        while pos > 0 and key < arr[pos - 1]:
            arr[pos] = arr[pos - 1]
            pos = pos - 1

        arr[pos] = key


arr = [11,2,3,4,1,56,8,1,9]

print(arr, "before sorting")
insertion(arr)
print(arr, "after sorting")
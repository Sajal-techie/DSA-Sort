def selection(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [5,4,22,1,4,7,9,5,1.1,1,0,]
print(arr, "Before sorting")
selection(arr)
print(arr, "After sorting")

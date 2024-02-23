def bubble(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]


arr = [1, 7, 3, 1, 5, 7, 100, 2, 1, 0]
print(arr, " before sorting",)
bubble(arr)
print(arr, " After sorting",)

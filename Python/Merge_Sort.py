def merge(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_list = arr[:mid]
        right_list = arr[mid:]
        merge(left_list)
        merge(right_list)
        i, j, k = 0, 0, 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                arr[k] = left_list[i]
                i += 1
                k += 1
            else:
                arr[k] = right_list[j]
                j += 1
                k += 1

        while i < len(left_list):
            arr[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            arr[k] = right_list[j]
            j += 1
            k += 1


arr = [4,1,4,7,9,0,.1,26,8,1,-1,-9]
print(arr, "before sorting")
merge(arr)
print(arr, "after sorting")
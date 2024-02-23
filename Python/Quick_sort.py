def pivot(arr, first, last):
    piv = arr[first]
    left = first + 1
    right = last
    while True:
        while left <= right and arr[left] <= piv:
            left += 1
        while left <= right and arr[right] >= piv:
            right -= 1
        if left > right:
            break
        else:
            arr[left],arr[right] = arr[right], arr[left]

    arr[first], arr[right] = arr[right], arr[first]
    return right


def quick(arr, first, last):
    if first < last:
        p = pivot(arr, first, last)
        quick(arr, first, p - 1)
        quick(arr, p + 1, last)


arr = [2,45,67,3,1,3,6,7,5,1,2,5]
print(arr, "before sorting")
quick(arr, 0, len(arr)-1)
print(arr, "after sorting")
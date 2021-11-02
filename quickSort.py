def quickSort(arr, lo, hi):
    if(lo < hi):
        p = partition(arr, lo, hi)
        quickSort(arr, lo, p-1)
        quickSort(arr, p+1, hi)


def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
    temp = arr[i]
    arr[i] = arr[hi]
    arr[hi] = temp
    return i

def merge(arr,left,right):
    nl = len(left)
    nr = len(right)
    i = j = k = 0
    while(i<nl and j < nr):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        elif right[j] < left[i]:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < nl:
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < nr:
        arr[k] = right[j]
        j += 1
        k += 1
    
    return arr

def mergeSort(arr):
    n = len(arr)
    if n < 2:
        return arr
    mid = n//2
    left = arr[0:mid]
    right = arr[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(arr,left,right)
    
arr = mergeSort([7,1,1,1,5,4,3,2,99,41,23,43,9,8,-1,-2,-4,-99])
print(arr)
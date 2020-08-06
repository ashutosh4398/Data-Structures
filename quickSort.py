def partition(arr,start,end):
    # partition of an array
    pindx = start
    pivot = arr[end]
    for i in range(start,end-1+1):
        if arr[i] < pivot:
            # swap
            arr[i],arr[pindx] = arr[pindx],arr[i]
            pindx += 1
    # swap with the pivot
    arr[end],arr[pindx] = arr[pindx],arr[end]
    return pindx,arr

def QuickSort(arr,start,end):
    if start < end:
        p,arr = partition(arr,start,end)
        arr = QuickSort(arr,start,p-1)
        arr = QuickSort(arr,p+1,end)
    return arr

def main():
    arr = [7,2,1,6,8,5,3,4,10,0,13,15,-1,-2,-5]
    arr = QuickSort(arr,0,len(arr)-1)
    print(arr)

if __name__ == '__main__':
    main()
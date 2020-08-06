# Time complexity in all the cases is O(n^2)

def SelectionSort(arr):
    for i in range(len(arr)-1):
        minIndex = i
        
        for j in range(i+1,len(arr)):
            # find minimum index from i+1 to nth element
            if arr[j] < arr[minIndex]:
                minIndex = j
        # swap
        arr[i],arr[minIndex] = arr[minIndex],arr[i]

    return arr

def main():
    arr = [2,7,4,1,5,3]
    print(SelectionSort(arr))

if __name__ == '__main__':
    main()
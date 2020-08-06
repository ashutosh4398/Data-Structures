def InsertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        # holding the current element
        value = arr[i]
        hole = i
        while(hole > 0 and arr[hole-1] > value):
            arr[hole] = arr[hole-1]
            hole = hole - 1
        arr[hole] = value
    return arr

def main():
    arr = [7,2,4,1,5,3]
    arr = InsertionSort(arr)
    print(f"after sorting: {arr}")

if __name__ == '__main__':
    main()
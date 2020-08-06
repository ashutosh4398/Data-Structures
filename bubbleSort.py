""" 
Complexity analysis:
1. Best Case: if the array is already sorted then it will take O(n) time
                using the modified algo using flag variable
2. Average & Worst case: O(n^2) 

"""
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        # improving the complexity atleast in best case
        flag = False
        for j in range(n-1-i):
            # if there is swapping involved then flag = True
            if arr[j] > arr[j+1]:
                # swap
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = True
        # if there is no swapping it means that the array is sorted
        if flag == False:
            break
        print(f"At pass {i} arr = {arr}")
    return arr

def main():
    arr = [2,7,4,1,5,3]
    arr = bubbleSort(arr)
    print(f"After sorting : {arr}")


if __name__=='__main__':
    main()
def merge(arr,left,right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
            
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1
    
    while i < len(left):
        arr[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        arr[k] = right[j]
        j = j + 1
        k = k + 1

def mergesort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)
        merge(arr,left,right)

arr = list(map(int,input("Enter the unsorted array space seperated: ").split()))

print("The array before mergesort: ",arr)

mergesort(arr)

print("The array after mergesort: ",arr)
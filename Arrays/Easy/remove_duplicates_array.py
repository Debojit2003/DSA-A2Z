def removeduplicates(arr):
    l = 1
    for r in range(1,len(arr)):
        if arr[r] != arr[r-1]:
            arr[l] = arr[r]
            l = l + 1
    
    return l

arr = list(map(int,input("Enter the array: ").split()))
k = removeduplicates(arr)
print("After removing duplicates: ", arr[:k])
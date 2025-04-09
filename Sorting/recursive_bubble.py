def recursive_bubble(arr,n=None):
    if n is None:
        n = len(arr)
    
    if n == 1:
        return
    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    recursive_bubble(arr,n-1)

arr = list(map(int,input("Enter the unsorted array space seperated: ").split()))
recursive_bubble(arr)
print(arr)
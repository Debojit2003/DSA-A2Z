def right_rotate(arr, k):
    n = len(arr)
    k %= n
    if k == 0:
        return
    
    arr[:] = arr[::-1]
    arr[:k] = arr[:k][::-1]
    arr[k:] = arr[k:][::-1]

arr = list(map(int, input("Enter the arrays space separated: ").split()))
k = int(input("Enter the number of times: "))
right_rotate(arr, k)
print(arr)

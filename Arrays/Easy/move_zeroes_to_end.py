def push_zeroes(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
        
    while count < len(arr):
        arr[count] = 0
        count += 1
    return arr

arr = list(map(int,input("Enter the arrays space seperated: ").split()))
print(arr)
push_zeroes(arr)
print(arr)
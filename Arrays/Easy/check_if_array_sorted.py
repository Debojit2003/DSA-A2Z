def is_sorted_check(arr):
    N = len(arr)
    count = 1
    for i in range(1,2*N):
        if arr[(i-1)%N] <= arr[i%N]:
            count += 1
        else:
            count = 1
        
        if count == N:
            return True
    
    return N == 1

arr = list(map(int,input("Enter the array elements comma seperated: ").split()))
print(is_sorted_check(arr))
        
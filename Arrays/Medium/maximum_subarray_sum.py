def subarray_sum(arr):
    
    max_subarray = arr[0]
    current_sum = 0
    result = []

    for i in arr:
        if current_sum < 0:
            current_sum = 0
        
        current_sum += i
        max_subarray = max(max_subarray, current_sum)
    
    return max_subarray

arr = list(map(int,input("Enter the values space seperated: ").split()))

print(subarray_sum(arr))

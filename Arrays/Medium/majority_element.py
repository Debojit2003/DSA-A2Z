def majority_element(nums):
    res,count = 0,0
    for n in nums:
        if count == 0:
            res = n
        
        count += (1 if n==res else -1)
    
    return res

nums = list(map(int,input("Enter the array: ").split()))
print(majority_element(nums))
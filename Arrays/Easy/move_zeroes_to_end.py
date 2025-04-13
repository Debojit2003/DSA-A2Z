#approach1
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

#approach2
def movezeros(nums):
        l=0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
        return nums
nums = list(map(int,input("Enter the arrays space seperated: ").split()))
movezeros(nums)

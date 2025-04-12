# def twosum(arr,target):
#     n = len(arr)
#     l1 = []
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i] + arr[j] == target:
#                 l1.append(i)
#                 l1.append(j)
    
#     return l1

# arr = list(map(int,input("Enter the array space seperated: ").split()))
# target = int(input("Enter the target: "))
# print(twosum(arr,target))

def two_sum(arr,target):
    prevMap = {}
    for i,n in enumerate(arr):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[n] = i
    
    return
arr = list(map(int,input("Enter the array space seperated: ").split()))
target = int(input("Enter the target: "))
print(two_sum(arr,target))

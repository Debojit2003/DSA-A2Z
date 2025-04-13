#approach1
def largest(arr):
    return max(arr)

arr = list(map(int,input("Enter the array elements comma seperated: ").split()))
print("Largest element is", largest(arr))

#approach2
def largest(arr):
    arr.sort()
    return arr[-1]
arr=list(map(int,input("Enter the elements comma seperated:").split()))
print("Largest element is:",largest(arr))

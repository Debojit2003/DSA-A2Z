def largest(arr):
    return max(arr)

arr = list(map(int,input("Enter the array elements comma seperated: ").split()))
print("Largest element is", largest(arr))
def linear(arr,k):
    for i in arr:
        if i == k:
            return True
    return False
    
arr = list(map(int,input("Enter the array space sepearated: ").split()))
k = int(input("Enter the number to search: "))
print(linear(arr,k))
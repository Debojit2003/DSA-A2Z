def singleXOR(arr):
    res = 0 #Here we are storing the XOR Value
    for i in arr:
        res = res ^ i #Here we are performing XOR operation on each element of the array
    return res

arr = list(map(int,input("Enter the array seperated by spaces: ").split()))
print("The Single element is: ",singleXOR(arr))
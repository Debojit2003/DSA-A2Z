def thrice_case(arr):
    ones,twos = 0,0
    for i in arr:
        #Bit manipulation method.
        ones = (ones ^ i) & ~twos
        twos = (twos ^ i) & ~ones
    
    return ones

arr = list(map(int,input("Enter the array seperated by spaces: ").split()))
print("The Single element is: ",thrice_case(arr))
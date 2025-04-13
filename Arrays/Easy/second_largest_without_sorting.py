def sec_large(arr):
    maxi = max(arr)
    secmax = []
    found = False
    for i in arr:
        if i < maxi:
            secmax.append(i)
            found = True
    
    return max(secmax) if found else -1

arr = list(map(int,input("Enter the array elements comma seperated: ").split(',')))
print(sec_large(arr))

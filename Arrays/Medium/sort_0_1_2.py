# One Pass Method.

def sortcode(arr):
    l,r = 0,len(arr)-1
    i = 0
    def swap(i,j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    while i <= r:
        if arr[i] == 0:
            swap(l,i)
            l = l + 1
            
        elif arr[i] == 2:
            swap(i,r)
            r = r - 1
            i = i - 1
            
        i = i + 1
    
    return arr

arr = list(map(int,input("Enter the unsorted 0,1,2 array: ").split()))
print(sortcode(arr))

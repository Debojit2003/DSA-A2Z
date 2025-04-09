arr = list(map(int,input("Enter the unsorted array space seperated: ").split()))

def insertion(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j] :
            arr[j+1] = arr[j]
            j = j - 1
            arr[j+1] = key

print("The array before insertion sorting: ",arr)
insertion(arr)
print("The array after insertion sort is: ",arr)
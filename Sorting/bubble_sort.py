arr = list(map(int,input("Enter the unsorted array space seperated: ").split()))

def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        is_sorted = True
        for j in range(n-i-1):
            is_sorted = False
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
        if is_sorted:
            return
        
print("The array before implementing bubble sort: ",arr)

bubble(arr)

print("The array after implementing bubble sort is: ",arr)
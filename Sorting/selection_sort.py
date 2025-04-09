arr = list(map(int,input("Enter the unsorted array space seperated: ").split()))

def selection(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if (arr[j]<arr[min_index]):
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]


print("The array before implementing selection sort: ",arr)
selection(arr)
print("The array after implementing selection sort: ",arr)
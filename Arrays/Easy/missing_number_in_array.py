def missing(arr):
    arr = set(arr)  # Converting to set for faster lookup
    i = 0
    while True:
        if i not in arr:
            return i
        i += 1

arr = list(map(int, input("Enter the numbers: ").split()))
print(missing(arr))
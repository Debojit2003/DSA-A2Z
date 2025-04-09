def arrayrot(arr,d):
    n = len(arr)

    d%=n

    arr[:d] = reversed(arr[:d])
    arr[d:] = reversed(arr[d:])

    arr.reverse()

    return arr

arr = list(map(int,input("Enter space seperated value: ").split()))
d = int(input("Enter the number of times to be rotated: "))
print(arrayrot(arr,d))
import math
def rotationArr(arr,d):
    n = len(arr)
    #Handle the case where d > size of array
    d%=n

    #Calculate the number of cycles in the rotation
    cycles = math.gcd(n,d)

    #Process each cycle
    for i in range(cycles):

        #Start element of current cycle
        start = arr[i]

        #Start index of current cycle
        current = i

        #Rotate elements till the end of the cycle
        while True:
            next = (current + d) % n

            if next == i:
                break
            arr[current] = arr[next]
            current = next

        #Copy the start element of current cycle at the last
        #index of the cycle
        arr[current] = start
    return arr

arr = list(map(int,input("Enter space seperated value: ").split()))
d = int(input("Enter the number of times to be rotated: "))
print(rotationArr(arr,d))
#rotationArr(arr,d)
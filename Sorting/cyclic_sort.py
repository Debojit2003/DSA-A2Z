def cyclic_sort(arr):
    n = len(arr)
    for cyclestart in range(0,n-1):
        item = arr[cyclestart]
        pos = cyclestart
        for i in range(cyclestart+1,n):
            if arr[i] < item:
                pos += 1
        
        if pos == cyclestart:
            continue

        while item == arr[pos]:
            pos += 1
        arr[pos],item = item,arr[pos]

        while pos != cyclestart:
            pos = cyclestart
            for i in range(cyclestart+1,n):
                if arr[i] < item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos],item = item,arr[pos]

    return arr

arr = list(map(int,input("Enter the space seperated value: ").split()))

c = cyclic_sort(arr)
print(c)
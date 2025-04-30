def subarray_sum(arr):
    max_sum = current_sum = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if current_sum < 0:
            current_sum = arr[i]
            s = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i

    return max_sum, arr[start:end+1]

arr = list(map(int, input("Enter the values space separated: ").split()))
print(subarray_sum(arr))

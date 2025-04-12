def getLongestSubarray(a, k):
    n = len(a)               # n = 10 → array has 10 elements
    left, right = 0, 0       # start both pointers at index 0
    Sum = a[0]               # Sum = 1 (a[0])
    maxLen = 0               # to store the max length of subarray with sum = k

    while right < n:         # continue while right pointer is within array

        while left <= right and Sum > k:
            # shrink the window from left if sum is more than k
            Sum -= a[left]   # remove value at left pointer
            left += 1        # move left pointer to the right

        if Sum == k:
            # if current subarray sum is equal to k
            maxLen = max(maxLen, right - left + 1)  # update maxLen if needed

        right += 1           # move right pointer to the right (expand window)
        if right < n:
            Sum += a[right]  # add next element to sum

    return maxLen            # return longest valid subarray length

# Test it with your new inputs
# a = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
# k = 3
a = list(map(int,input("Enter the array as asked seperated by spaces: ").split()))
k = int(input("Enter the target sum: "))
print(getLongestSubarray(a, k))

print("Longest Sub array is: ", getLongestSubarray(a, k))

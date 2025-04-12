#https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1

def longest(arr,k):
        sum_index = {}
        prefix_sum = 0
        max_len = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum == k:
                max_len = i + 1  # whole subarray from start

            if (prefix_sum - k) in sum_index:
                length = i - sum_index[prefix_sum - k]
                max_len = max(max_len, length)

            # store only first occurrence of prefix_sum
            if prefix_sum not in sum_index:
                sum_index[prefix_sum] = i

        return max_len

arr = list(map(int,input("Enter the array as asked seperated by spaces: ").split()))
k = int(input("Enter the target sum: "))
print(longest(arr, k))
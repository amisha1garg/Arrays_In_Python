# Given an array Arr of N positive integers, find K largest elements from the array.  The output elements should be printed in decreasing order.
#
# Example 1:
#
# Input:
# N = 5, K = 2
# Arr[] = {12, 5, 787, 1, 23}
# Output: 787 23
# Explanation: 1st largest element in the
# array is 787 and second largest is 23.

# User function Template for python3
class Solution:

    def kLargest(self, arr, n, k):
        # code here
        x = []
        arr.sort(reverse=True)
        # 		for i in range(n):

    for j in range(k):
        x.append(arr[j])
    return x


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
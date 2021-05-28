# You are given an array Arr of size N. Find the sum of distinct elements in an array.
#
# Example 1:
#
# Input:
# N = 5
# Arr[] = {1, 2, 3, 4, 5}
# Output: 15
# Explanation: Distinct elements are 1, 2, 3
# 4, 5. So sum is 15.

# User function Template for python3
class Solution:

    def findSum(self, arr, n):
        # code here
        arr = set(arr)
        return sum(arr)


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
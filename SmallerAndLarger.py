# Given a sorted array Arr of size N and a value X, find the number of array elements less than or equal to X and elements more than or equal to X.
#
# Example 1:
#
# Input:
# N = 7, X = 0
# Arr[] = {1, 2, 8, 10, 11, 12, 19}
# Output: 0 7
# Explanation: There are no elements less or
# equal to 0 and 7 elements greater or equal
# to 0.
# User function Template for python3
class Solution:

    def getMoreAndLess(self, arr, n, x):
        # code here
        c = count = 0
        for i in range(n):
            if arr[i] >= x:
                count += 1
            if arr[i] <= x:
                c += 1
        return c, count


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMoreAndLess(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends

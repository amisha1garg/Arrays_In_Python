# Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.
#
# Example 1:
#
# Input:
# N = 7, X = 2
# Arr[] = {1, 1, 2, 2, 2, 2, 3}
# Output: 4
# Explanation: 2 occurs 4 times in the
# given array

#User function Template for python3
class Solution:

	def count(self,arr, n, x):
		# code here
# 		for i in range(n):
	    return arr.count(x)

#{
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends
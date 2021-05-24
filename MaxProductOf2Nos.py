# Given an array Arr of size N with all elements greater than or equal to zero. Return the maximum product of two numbers possible.
#
# Example 1:
#
# Input:
# N = 6
# Arr[] = {1, 4, 3, 6, 7, 0}
# Output: 42

#User function Template for python3
class Solution:

	def maxProduct(self,arr, n):
		# code here
		arr.sort()
		return arr[n-1]*arr[n-2]

#{
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
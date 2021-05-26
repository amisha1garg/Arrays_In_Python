# Provided an array Arr of N integers, you need to reverse a subarray of that array. The range of this subarray is given by L and R.
#
# Example 1:
#
# Input:
# N = 7
# Arr[] = {1, 2, 3, 4, 5, 6, 7}
# L = 2, R = 4
# Output:
# 1 4 3 2 5 6 7
# Explanation: After reversing the elements
# in range 2 to 4 (2, 3, 4),
# modified array is 1, 4, 3, 2, 5, 6, 7.

#User function Template for python3
class Solution:

	def reverseSubArray(self,arr, n, l, r):
		# code here

	    arr[l-1:r]=arr[l-1:r][::-1]
	    return arr[:]

#{
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        l, r = list(map(int, input().strip().split()))
        ob = Solution()
        ob.reverseSubArray(arr, n, l, r)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
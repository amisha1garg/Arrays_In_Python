# Given an array of even size N, task is to find minimum value that can be added to an element so that array become balanced. An array is balanced if the sum of the left half of the array elements is equal to the sum of right half.
#
#
# Example 1:
#
# Input:
# N = 4
# arr[] = {1, 5, 3, 2}
# Output: 1
# Explanation:
# Sum of first 2 elements is 1 + 5  = 6,
# Sum of last 2 elements is 3 + 2  = 5,
# To make the array balanced you can add 1.

#User function Template for python3

class Solution:
    def minValueToBalance(self,a,n):
        #code here.
        s=0
        x=0
        for i in range(0,(int(n/2))):
            s= s+a[i]
        for j in range(int(n/2),n):
            x += a[j]
        if s==x:
            return 0
        else:
            return abs(s-x)

#{
#  Driver Code Starts
#Initial Template for Python 3





t=int(input())
for _ in range(0,t):
    n=int(input())
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.minValueToBalance(a,n)
    print(ans)

# } Driver Code Ends
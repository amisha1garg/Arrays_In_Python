#User function Template for python3
# Given an integer array Arr[] of size N. The task is to find sum of it.
from numpy import *
class Solution:

	def _sum(self,arr, n):
   		# code here
   		return sum(arr)


#{
#  Driver Code Starts
#Initial Template for Python 3




# Driver code
if __name__ == "__main__":
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        ob = Solution()
        ans = ob._sum(a
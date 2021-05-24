# Given an array of N positive integers where all numbers occur even number of times except one number which occurs odd number of times. Find the exceptional number.
#
# Example 1:
#
# Input:
# N = 7
# Arr[] = {1, 2, 3, 2, 3, 1, 3}
# Output: 3

#User function Template for python3
from collections import Counter
class Solution:
    def getOddOccurrence(self, arr, n):
        # code here
        dt=Counter(arr)
        for i in dt:
            if dt[i]%2!=0:
                return i

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getOddOccurrence(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
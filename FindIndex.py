# Given an unsorted array Arr[] of N integers and a Key which is present in this array. You need to write a program to find the start index( index where the element is first found from left in the array ) and end index( index where the element is first found from right in the array ).
#
# Example 1:
#
# Input:
# N = 6
# arr[] = { 1, 2, 3, 4, 5, 5 }
# Key = 5
# Output:  4 5
# Explanation:
# 5 appears first time at index 4 and
# appears last time at index 5.
# (0 based indexing)
# User function Template for python3

class Solution:
    def findIndex(self, a, N, key):
        # code here.
        k = -1
        l = -1
        for i in range(N):
            if a[i] == key:
                k = i
                break
        for j in reversed(range(N)):
            if a[j] == key:
                l = j
                break
        return (k, l)


# {
#  Driver Code Starts
# Initial Template for Python 3


t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    key = int(input())
    ob = Solution()
    ans = ob.findIndex(a, n, key)
    print(*ans)

# } Driver Code Ends
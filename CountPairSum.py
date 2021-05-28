# Given two sorted arrays(arr1[] and arr2[]) of size M and N of distinct elements. Given a value Sum. The problem is to count all pairs from both arrays whose sum is equal to Sum.
# Note: The pair has an element from each array.
#
#
# Example 1:
#
# Input:
# M=4, N=4 , Sum = 10
# arr1[] = {1, 3, 5, 7}
# arr2[] = {2, 3, 5, 8}
# Output: 2
# Explanation: The pairs are: (5, 5) and (7, 3).

# User function Template for python3

class Solution:
    def countPairs(self, arr1, arr2, M, N, x):
        # code here.
        count = 0
        store = set()
        for i in range(M):
            store.add(arr1[i])
        for j in range(N):
            if x - arr2[j] in store:
                count += 1
        return count


# {
#  Driver Code Starts
# Initial Template for Python 3


t = int(input())
for _ in range(0, t):
    m, n = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = int(input())
    ob = Solution()
    print(ob.countPairs(a, b, m, n, x))

# } Driver Code Ends
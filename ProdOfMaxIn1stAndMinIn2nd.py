# Given two arrays of A and B respectively of sizes N1 and N2, the task is to calculate the product of the maximum element of the first array and minimum element of the second array.
#
# Example 1:
#
# Input : A[] = {5, 7, 9, 3, 6, 2},
#         B[] = {1, 2, 6, -1, 0, 9}
# Output : -9
# Explanation:
# The first array is 5 7 9 3 6 2.
# The max element among these elements is 9.
# The second array is 1 2 6 -1 0 9.
# The min element among these elements is -1.
# The product of 9 and -1 is 9*-1=-9.

# User function Template for python3

class Solution:
    def find_multiplication(self, arr, brr, n, m):
        # Complete the function
        x = max(arr)
        y = min(brr)
        return x * y


# {
#  Driver Code Starts
# Initial Template for Python 3


for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    m = int(input())
    brr = list(map(int, input().strip().split()))
    ob = Solution()
    res = ob.find_multiplication(arr, brr, n, m)
    print(res)

# } Driver Code Ends
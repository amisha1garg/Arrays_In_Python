# Given an integer array and another integer element. The task is to find if the given element is present in array or not.
#
# Example 1:
#
# Input:
# n = 4
# arr[] = {1,2,3,4}
# x = 3
# Output: 2
# Explanation: There is one test case
# with array as {1, 2, 3 4} and element
# to be searched as 3.  Since 3 is
# present at index 2, output is 2.

# User function Template for python3

class Solution:
    # Complete the below function
    def search(self, arr, N, X):
        # Your code here
        for i in range(0, N):
            if X in arr:
                return arr.index(X)
            else:
                return -1


# {
#  Driver Code Starts
# Initial Template for Python 3


import math


def main():
    T = int(input())
    while (T > 0):
        N = int(input())

        A = [int(x) for x in input().strip().split()]

        x = int(input())
        ob = Solution()
        print(ob.search(A, N, x))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
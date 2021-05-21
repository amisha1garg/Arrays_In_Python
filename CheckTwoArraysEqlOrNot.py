# Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.
# Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.
#
# Example 1:
#
# Input:
# N = 5
# A[] = {1,2,5,4,0}
# B[] = {2,4,5,0,1}
# Output: 1
# Explanation: Both the array can be
# rearranged to {0,1,2,4,5}


# User function Template for python3

class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, A, B, N):
        A.sort()
        B.sort()
        for i in range(N):
            if A[i] != B[i]:
                return False
        return True

        # return: True or False

        # code here


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tc in range(t):

        N = int(input())

        A = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        ob = Solution()
        if ob.check(A, B, N):
            print(1)
        else:
            print(0)

# } Driver Code Ends
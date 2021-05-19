# Given a sorted array A of size N, delete all the duplicates elements from A.
#
#
# Example 1:
#
# Input:
# N = 5
# Array = {2, 2, 2, 2, 2}
# Output: 2
# Explanation: After removing all the duplicates
# only one instance of 2 will remain.
#User function template for Python

class Solution:
	def remove_duplicate(self, B, N):
		# code here
        global A
        A=dict.fromkeys(B)
        A=list(A)
        A.sort()
        return(len(A))
#{
#  Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends
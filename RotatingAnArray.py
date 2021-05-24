# Given an array of size N. The task is to rotate array by D elements where D ≤ N.
#
# Example 1:
#
# Input:
# N = 7
# Arr[] = {1, 2, 3, 4, 5, 6, 7}
# D = 2
# Output: 3 4 5 6 7 1 2
# Explanation:
# Rotate by 1: [2, 3, 4, 5, 6, 7, 1]
# Rotate by 2: [3, 4, 5, 6, 7, 1, 2]


#User function Template for python3

class Solution:
    def leftRotate(self, arr, n, d):
        # code here
        arr[:]=arr[d:n]+arr[0:d]
        return arr

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        d = int(input())
        ob = Solution()
        ob.leftRotate(arr, n, d)
        for xx in arr:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
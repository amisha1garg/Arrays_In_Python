# Given an array Arr of size N, print second largest element from an array.
#
# Example 1:
#
# Input:
# N = 6
# Arr[] = {12, 35, 1, 10, 34, 1}
# Output: 34
# Explanation: The largest element of the
# array is 35 and the second largest element
# is 34.
# User function Template for python3
class Solution:

    def print2largest(self, arr, n):
        # code here
        mini = -99999999999
        first = mini
        second = mini
        for i in range(0, n):
            if (arr[i] > first):
                second = first
                first = arr[i]
            elif (arr[i] >= second and arr[i] < first):
                second = arr[i]
        #  else :
        #      first = first
        #      second = second

    if second == -99999999999:
        return -1
    else:
        return second


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
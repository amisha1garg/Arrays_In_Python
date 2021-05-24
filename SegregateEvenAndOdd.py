# Given an array Arr[], write a program that segregates even and odd numbers. The program should put all even numbers first in sorted order, and then odd numbers in sorted order.
#
# Example 1:
#
# Input:
# N = 7
# Arr[] = {12, 34, 45, 9, 8, 90, 3}
# Output: 8 12 34 90 3 9 45
# Explanation: Even numbers are 12, 34,
# 8 and 90. Rest are odd numbers. After
# sorting even numbers 8 12 34 90 and
# after sorting odd numbers 3 9 45. Then
# concat both.

# User function Template for python3
class Solution:

    def segregateEvenOdd(self, arr, n):
        # code here
        x = []
        y = []
        for i in range(n):
            if arr[i] % 2 == 0:
                x.append(arr[i])
        else:
            y.append(arr[i])

    x.sort()
    y.sort()
    arr[:] = x[:] + y[:]
    return


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregateEvenOdd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
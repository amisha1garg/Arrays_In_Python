# You are given an array Arr of size N. Replace every element with the next greatest element (greatest element on its right side) in the array. Also, since there is no element next to the last element, replace it with -1.
#
# Example 1:
#
# Input:
# N = 6
# Arr[] = {16, 17, 4, 3, 5, 2}
# Output:
# 17 5 5 5 2 -1
# Explanation: For 16 the greatest element
# on its right is 17. For 17 it's 5.
# For 4 it's 5. For 3 it's 5. For 5 it's 2.
# For 2 it's -1(no element to its right).
# So the answer is 17 5 5 5 2 -1

# User function Template for python3
class Solution:

    def nextGreatest(self, arr, n):
        # code  here
        maxi = arr[n - 1]
        arr[n - 1] = -1
        for i in range(n - 2, -1, -1):
            temp = arr[i]

    arr[i] = maxi

    if (temp > maxi):
        maxi = temp
    return arr


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.nextGreatest(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
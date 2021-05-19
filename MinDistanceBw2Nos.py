# Minimum distance between two numbers
# You are given an array A, of N elements. Find minimum index based distance between two elements of the array, x and y.
#
# Example 1:
#
# Input:
# N = 4
# A[] = {1,2,3,2}
# x = 1, y = 2
# Output: 1
# Explanation: x = 1 and y = 2. There are
# two distances between x and y, which are
# 1 and 3 out of which the least is 1.


import sys


class Solution:
    # def minDist(self, a, n, x, y):
    #     if(x not in a or y not in a ):
    #         return (-1)
    #     else:
    #         t=[]
    #         t1=[]
    #         for i in range(n):
    #             if(a[i]==x):
    #                 t.append(i)
    #             elif(a[i]==y):
    #                 t1.append(i)
    #         min=10000000
    #         for i in t:
    #             for j in t1:
    #                 r=abs(i-j)
    #                 if(r<min):
    #                     min=r
    #                     return min

    def minDist(self, arr, n, x, y):

        # previous index and min distance
        i = 0
        p = -1
        min_dist = sys.maxsize;

        for i in range(n):

            if (arr[i] == x or arr[i] == y):

                # we will check if p is not equal to -1 and
                # If the element at current index matches with
                # the element at index p , If yes then update
                # the minimum distance if needed
                if (p != -1 and arr[i] != arr[p]):
                    min_dist = min(min_dist, i - p)

                # update the previous index
                p = i

        # If distance is equal to int max
        if (min_dist == sys.maxsize):
            return -1
        return min_dist


# # Driver program to test above function */
# arr = [3, 5, 4, 2, 6, 3, 0, 0, 5, 4, 8, 3]
# n = len(arr)
# x = 3
# y = 6
# print ("Minimum distance between %d and %d is %d\n"%( x, y,minDist(arr, n, x, y)));

# This code is contributed by Shreyanshi Arun.


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x, y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))

# } Driver Code Ends
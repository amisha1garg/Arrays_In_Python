# Given
# an
# array
# arr[]
# of
# N
# distinct
# integers, output
# the
# array in such
# a
# way
# that
# the
# first
# element is first
# maximum and the
# second
# element is the
# first
# minimum, and so
# on.
#
# Example
# 1:
#
# Input: N = 7, arr[] = {7, 1, 2, 3, 4,
#                        5, 6}
# Output: 7
# 1
# 6
# 2
# 5
# 3
# 4
# Explanation: The
# first
# element is first
# maximum and second
# element is first
# minimum and so
# on.


# class Solution:
def alternateSort(arr, N):
    # Your code goes here
    arr.sort()
    a = []
    x = 0
    y = N - 1
    while x < y:
        a.append(arr[y])
        a.append(arr[x])
        x += 1
        y -= 1
    if N % 2 != 0:
        a.append(arr[x])
    return a


# {
#  Driver Code Starts
if __name__ == '__main__':
    def printAns(ans):
        for x in ans:
            print(x, end=" ");
        print()


    t = int(input())
    for _ in range(0, t):
        n = int(input())
        a = list(map(int, input().split()))
        ans = alternateSort(a, n)
        printAns(ans)
# } Driver Code Ends
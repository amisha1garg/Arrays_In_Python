# Given
# an
# array
# arr[]
# of
# size
# N, the
# task is to
# add
# the
# minimum
# number(should
# be
# greater
# than
# 0) to
# the
# array
# so
# that
# the
# sum
# of
# the
# array
# becomes
# even
#
# Example
# 1:
#
# Input: N = 8
# arr[] = {1, 2, 3, 4, 5, 6, 7, 8}
# Output: 2
# Explanation: Sum
# of
# array is 36, so
# we
# add
# minimum
# number
# 2
# to
# make
# the
# sum
# even.


class Solution:
    def minNum(self, arr, n):
        # Your code goes here
        count = 0
        for i in range(n):
            if arr[i] % 2 != 0:
                count = count + 1
        if count % 2 == 0:
            return 2
        else:
            return 1


# {
#  Driver Code Starts
if __name__ == '__main__':

    t = int(input())
    for _ in range(0, t):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        ans = ob.minNum(a, n)
        print(ans)
# } Driver Code Ends
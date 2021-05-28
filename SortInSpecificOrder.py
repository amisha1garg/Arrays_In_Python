# Given
# an
# array
# A
# of
# positive
# integers.Your
# task is to
# sort
# them in such
# a
# way
# that
# the
# first
# part
# of
# the
# array
# contains
# odd
# numbers
# sorted in descending
# order, rest
# portion
# contains
# even
# numbers
# sorted in ascending
# order.
#
# Example
# 1:
#
# Input:
# N = 7
# Arr = {1, 2, 3, 5, 4, 7, 10}
# Output:
# 7
# 5
# 3
# 1
# 2
# 4
# 10
# Explanation:
# Array
# elements
# 7
# 5
# 3
# 1
# are
# odd
# and sorted in descending
# order,
# whereas
# 2
# 4
# 10
# are
# even
# numbers
# and sorted in ascending
# order.

# User function Template for python3

class Solution:
    def sortIt(self, arr, n):
        # code here.
        a = []
        b = []
        for i in range(n):
            if arr[i] % 2 == 0:
                a.append(arr[i])
            else:
                b.append(arr[i])

        a.sort()
        b.sort(reverse=True)
        arr[:] = b[:] + a[:]
        return arr


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortIt(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
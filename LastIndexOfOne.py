# Given
# a
# string
# S
# consisting
# only
# '0'
# s and '1'
# s, find
# the
# last
# index
# of
# the
# '1'
# present in it.
#
# Example
# 1:
#
# Input:
# S = 00001
# Output:
# 4
# Explanation:
# Last
# index
# of
# 1 in given
# string is 4.

# User function Template for python3

class Solution:
    def lastIndex(self, s):
        # code here
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                return i
        return -1


# {
#  Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())

    while (T > 0):
        s = input()
        ob = Solution()
        print(ob.lastIndex(s))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
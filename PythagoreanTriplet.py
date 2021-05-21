# Given an array arr of N integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2, otherwise false.
#
# Example 1:
#
# Input:
# N = 5
# Arr[] = {3, 2, 4, 6, 5}
# Output: Yes
# Explanation: a=3, b=4, and c=5 forms a
# pythagorean triplet.

# User function Template for python3
class Solution:

    def checkTriplet(self, arr, n):

    # code here
    arr.sort()
    x = [i ** 2 for i in arr]
    i = n - 1
    while (i >= 0):
        j = 0
        k = i - 1
        while (j < k):
            if (x[i] == x[j] + x[k]):
                return True

                # pair found

            elif (x[i] > x[j] + x[k]):
                j += 1
            else:
                k -= 1
        i -= 1
    return False


# 	for i in range(n):
# 	    for j in range(i+1,n):
# 	        if (arr[i]**2) + (arr[j]**2) in x:
# 	            return True
#         else:
#             return False

# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.checkTriplet(arr, n)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends
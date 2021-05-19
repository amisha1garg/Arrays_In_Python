# Given an array of distinct elements. Find the third largest element in it.
#
# Example 1:
#
# Input:
# N = 5
# A[] = {2,4,1,3,5}
# Output: 3


class Solution:
    def thirdLargest(self, a, n):
        # code here

        a.sort(reverse=True)
        if len(a) < 3:
            return -1
        return a[2]


# {
#  Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr, n))
# } Driver Code Ends
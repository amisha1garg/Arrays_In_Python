# Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to that of its index value.
#
# Example 1:
#
# Input:
# N = 5
# Arr[] = {15, 2, 45, 12, 7}
# Output: 2
# Explanation: Only Arr[2] = 2 exists here.

# User function Template for python3
class Solution:

    def valueEqualToIndex(self, arr, n):
        # code here
        a = []
        arr.insert(0, 0)
        for i in range(1, len(arr)):

            # 		for i,v in enumerate(arr,1):
            if i == arr[i]:
                a.append(i)

    return a


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.valueEqualToIndex(arr, n)
        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x, end=" ")
            print()
        tc -= 1

# } Driver Code Ends
# Given an array Arr of N positive integers and a number K where K is used as a threshold value to divide each element of the array into sum of different numbers. Find the sum of count of the numbers in which array elements are divided.
#
# Example 1:
#
# Input:
# N = 4, K = 3
# Arr[] = {5, 8, 10, 13}
# Output: 14
# Explanation: Each number can be expressed as sum
# of different numbers less than or equal to K as
# 5 (3 + 2), 8 (3 + 3 + 2), 10 (3 + 3 + 3 + 1),
# 13 (3 + 3 + 3 + 3 + 1). So, the sum of count
# of each element is (2+3+4+5)=14.

#User function Template for python3

class Solution:
    def totalCount(self, arr, n, k):
        # code here
        count = 0
        for i in range(n):
            x = arr[i]/k
            if float(x)>int(x):
                count += int(x) + 1
            else :
                count+= int(x)
        return count

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.totalCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
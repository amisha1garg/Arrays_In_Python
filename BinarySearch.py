# User function template for Python
# Given a sorted array of size N and an integer K, find the position at which K is present in the array using binary search.
#
#
# Example 1:
#
# Input:
# N = 5
# arr[] = {1 2 3 4 5}
# K = 4
# Output: 3
# Explanation: 4 appears at index 3.


class Solution:
    def binarysearch(self, arr, n, k):
        low = 0

        high = len(arr) - 1
        mid = 0

        while low <= high:

            mid = (high + low) // 2

            # If x is greater, ignore left half
            if arr[mid] < k:
                low = mid + 1

            # If x is smaller, ignore right half
            elif arr[mid] > k:
                high = mid - 1

            # means x is present at mid
            else:
                 return(mid)

        # If we reach here, then the element was not present
        return -1


# {
#  Driver Code Starts
# Initial template for Python

if __name__ == '__main__':
    t = int(input("t "))
    for i in range(t):
        n = int(input("n "))
        arr = list(map(int, input("arr ").strip().split(' ')))
        k = int(input("k "))
        ob = Solution()
        print(ob.binarysearch(arr, n, k))

# } Driver Code Ends
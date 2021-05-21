# Given an array A[]  of n elements. Your task is to complete the Function num which returns an integer denoting the total number of times digit k appears in the whole array.
#
# For Example:
# Input:
# A[]={11,12,13,14,15}, k=1
# Output:
# 6
#
# Explanation: Here digit 1 appers
# the whole array 6 times.

# Your task is to complete this function
# Function should return an integer
def num(arr, n, k):
    # Code here
    count = 0
    for i in range(n):
        x = str(arr)

    return x.count(str(k))


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        print(num(arr, n, k))
# Contributed By: Harshit Sidhwa

# } Driver Code Ends
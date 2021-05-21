# Given an array A of integers. Find three numbers such that sum of two elements equals the third element and return the triplet in a container result, if no such triplet is found return the container as empty.
#
# Input:
# First line of input contains number of testcases. For each testcases there will two lines. First line contains size of array and next line contains array elements.
#
# Output:
# For each test case output the triplets, if any triplet found from the array, if no such triplet is found, output -1.
#
# Your Task: Your task is to complete the function to find triplet and return container containing result.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 103
# 0 <= Ai <= 105
#
# Example:
# Input:
# 3
# 5
# 1 2 3 4 5
# 3
# 3 3 3
# 6
# 8 10 16 6 15 25
#
# Output:
# 1
# -1
# 1
#
# Explanation:
# Testcase 1:
# Triplet Formed: {2, 1, 3}
# Hence 1
# Test Case 2:
# Triplet Formed: {}
# Hence -1
# Test Case 3:
# Triplet Formed: {10, 15, 25}
# Hence 1


# User function Template for python3

# function should return a triplet
# if no such triplet is found return
# a container results as empty
def findTriplet(arr, n):
    # your code here

    # # x=[i for i in arr]
    # for i in range(n):
    #     for j in range(i+1,n):
    #         z=(arr[i]+ arr[j])
    #         if z in arr:
    #             a.append(arr[i])
    #             a.append(arr[j])
    #             a.append(z)

    arr.sort()
    a = []

    # for every element in arr
    # check if a pair exist(in array) whose
    # sum is equal to arr element
    i = n - 1
    while (i >= 0):
        j = 0
        k = i - 1
        while (j < k):
            if (arr[i] == arr[j] + arr[k]):

                # pair found
                a.append(arr[i])
                a.append(arr[j])
                a.append(arr[k])

                return a
            elif (arr[i] > arr[j] + arr[k]):
                j += 1
            else:
                k -= 1
        i -= 1
    return a


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for j in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = findTriplet(arr, n)
        if (len(a) == 3):
            print(1)
        else:
            print(-1)
# } Driver Code Ends
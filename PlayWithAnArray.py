# Given an unsorted array arr of size N, rearrange the elements of array such that number at the odd index is greater than the number at the previous even index. The task is to complete the function formatArray() which will return formatted array.
#
# NOTE:
# If the array formed is according to rules print 1, else 0.
#
# Example 1:
#
# Input:
# n = 5
# arr[] = {5, 4, 3, 2, 1}
#
# Output:
# 1
# Explanation:
# The given array after modification
# will be as such: 4 5 2 3 1.

def formatArray(a, n):
    # add code here
    for i in range(n - 1):
        if i % 2 == 0:
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        # print(a[i])
    return a


# {
#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for j in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = formatArray(a, n)
        flag = 1
        if (len(b) == len(a)):
            for k in range(1, n, 2):
                if (b[k] < b[k - 1]):
                    flag = 0
            if (flag == 0):
                print(0)
            else:
                b.sort()
                a.sort()
                for p in range(0, n):
                    if (a[p] != b[p]):
                        flag = 0
                print(flag)
        else:
            print(0)

# } Driver Code Ends
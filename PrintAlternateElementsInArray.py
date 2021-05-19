# You are given an array A of size N. You need to print elements of A in alternate order (starting from index 0).
#
# Example 1:
#
# Input:
# N = 4
# A[] = {1, 2, 3, 4}
# Output:
# 1 3
# Example 2:
#
# Input:
# N = 5
# A[] = {1, 2, 3, 4, 5}
# Output:
# 1 3 5

# arr is the array
# n is the number of elements in array
def printAl(arr,n):
    for i in range(0,n,2):
        print(arr[i], end= " ")
    return

#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        printAl(arr,n)
        print()
# } Driver Code Ends
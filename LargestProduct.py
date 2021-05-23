# Given an array consisting of N positive integers, and an integer k .You have to find the maximum product of k contiguous elements in the array. Your task is to complete the function which takes three arguments .The first argument  is the array A[ ] and second argument is an integer N denoting the size of the array A[ ] and the third argument  is an integer k.The function will return and value denoting the largest product of sub-array of size k.
#
# Input:
# The first line of input is an integer T denoting the no of test cases. Then T test casesfollow . The first line of each test case are two integer N and K separated by space .The next line contains N space separated values of the array A[ ].
#
# Output:
# Output of each test case will be an integer denoting the largest product of subarray of size k.
#
# Constraints:
# 1 <=T<= 100
# 1 <=N<= 10
# 1 <=K<= N
# 1<=A[]<=10
#
# Example:
# Input
# 1
# 4 2
# 1 2 3 4
# Output
# 12


# You are required to complete this fucntion
# Function should return the an integer
def findMaxProduct(arr, n, m):
    # Code here
    p=[]
    x=1
    z=0
    for i in range(n-m+1):
        for j in range(m):
            x = x * arr[i+j]
        p.append(x)
        x=1
        i+=1
        z=max(p)
    return z

#{
#  Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m = map(int, input().strip().split(' '))
        arr = list(map(int, input().strip().split()))
        print (findMaxProduct(arr, n, m))
# } Driver Code Ends
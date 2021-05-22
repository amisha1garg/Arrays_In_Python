# Given an array A of size N, construct a Sum Array S(of same size) such that S is equal to the sum of all the elements of A except A[i]. Your task is to complete the function SumArray(A, N) which accepts the array A and N(size of array).
# 
# Example 1:
# 
# Input:
# 5
# 3 6 4 8 9
# Output: 27 24 26 22 21
# Explanation: For the sum array S, at i=0 we
# have 6+4+8+9. At i=1, 3+4+8+9. At i=2, we 
# have 3+6+8+9. At i=3, we have 3+6+4+9. At
# i = 4, we have 3+6+4+8. So S is 27 24 26 22 21.

# User function Template for python3

# arr is the array
# n is the number of element in array
def SumArray(arr, n):
    # your code here

    sum = 0;
    for i in range(n):
        sum = sum + int(arr[i]);
    for i in range(n):
        print(sum - int(arr[i]), end=" ")


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    t = int(input())

    while (t >= 1):
        n = int(input())
        arr = input().split();
        SumArray(arr, n)
        print()
        t -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends
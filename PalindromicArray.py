# Given a Integer array A[] of n elements. Your task is to complete the function PalinArray. Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.
#
# Input:
# The first line of input contains an integer denoting the no of test cases. Then T test cases follow. Each test case contains two lines. The first line of input contains an integer n denoting the size of the arrays. In the second line are N space separated values of the array A[].
#
# Output:
# For each test case in a new line print the required result.

# Your task is to complete this function
# Function should return True/False or 1/0

def isPalindrome(N):
    str1 = "" + str(N)
    len1 = len(str1)
    for i in range(int(len1 / 2)):
        if (str1[i] != str1[len1 - 1 - i]):
            return False
    return True


def PalinArray(arr, n):
    # Code here
    for i in range(n):
        ans = isPalindrome(arr[i])
        if ans == False:
            return False
    return True


# {
#  Driver Code Starts
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)


# } Driver Code Ends
# Given
# an
# array
# A
# of
# size
# N
# of
# integers.Your
# task is to
# find
# the
# minimum and maximum
# elements in the
# array.
#
# Example
# 1:
#
# Input:
# N = 6
# A[] = {3, 2, 1, 56, 10000, 167}
# Output:
# min = 1, max = 10000

# User function Template for python3

def getMinMax(a, n):
    return min(a), max(a)


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]

        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
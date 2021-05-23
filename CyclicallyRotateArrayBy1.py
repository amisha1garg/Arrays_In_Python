# Given
# an
# array, rotate
# the
# array
# by
# one
# position in clock - wise
# direction.
#
# Example
# 1:
#
# Input:
# N = 5
# A[] = {1, 2, 3, 4, 5}
# Output:
# 5
# 1
# 2
# 3
# 4


# User function Template for python3

def rotate(arr, n):
    x = arr[n - 1]
    arr.pop()  # arr[n-1])
    arr.insert(0, x)

    return arr


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
# You are given an integer N. You need to convert all zeroes of N to 5.
#
# Example 1:
#
# Input:
# N = 1004
# Output: 1554
# Explanation: There are two zeroes in 1004
# on replacing all zeroes with "5", the new
# number will be "1554".

# Function should return an integer value
def convertFive(n):
    # Code here

    y = [int(x) for x in str(n)]
    for i in range(len(y)):
        if y[i] == 0:
            y[i] = 5
    s = [str(j) for j in y]

    # Join list items using join()
    n = int("".join(s))
    return n


# {
#  Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        print(convertFive(int(input().strip())))
# } Driver Code Ends
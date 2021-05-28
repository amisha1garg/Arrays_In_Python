# As we know, Ishaan has a love for chocolates. He has bought a huge chocolate bar that contains N chocolate squares. Each of the squares has a tastiness level which is denoted by an array A[].
# Ishaan can eat the first or the last square of the chocolate at once. Ishaan has a sister who loves chocolates too and she demands the last chocolate square. Now, Ishaan being greedy eats the more tasty square first.
# Determine the tastiness level of the square which his sister gets.
#
# Example 1:
#
# â€‹Input : arr[ ] = {5, 3, 1, 6, 9}
# Output : 1
# Explanation:
# Initially: 5 3 1 6 9
# In first step: 5 3 1 6
# In Second step: 5 3 1
# In Third step: 3 1
# â€‹In Fourth step: 1
# â€‹â€‹Return 1


# User function Template for python3

def chocolates(arr, n):
    # Complete the function
    return min(arr)


# {
#  Driver Code Starts
# Initial Template for Python 3


for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = chocolates(arr, n)
    print(ans)

# } Driver Code Ends
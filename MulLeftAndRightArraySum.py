# Pitsy needs help in the given task by her teacher. The task is to divide a array into two sub array (left and right) containing n/2 elements each and do the sum of the subarrays and then multiply both the subarrays.
#
# Example 1:
#
# â€‹Input : arr[ ] = {1, 2, 3, 4}
# Output : 21
# Explanation:
# Sum up an array from index 0 to 1 = 3
# Sum up an array from index 2 to 3 = 7
# Their multiplication is 21.â€‹â€‹

# User function Template for python3

def multiply(arr, n):
    # Complete the function
    x = sum(arr[0:n // 2])
    y = sum(arr[n // 2:n])
    return x * y


# {
#  Driver Code Starts
# Initial Template for Python 3


for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = multiply(arr, n)
    print(ans)
# } Driver Code Ends
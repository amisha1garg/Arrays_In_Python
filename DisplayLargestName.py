# Given a list of names, display the longest name.
#
#
# Example:
#
# Input:
# N = 5
# names[] = { "Geek", "Geeks", "Geeksfor",
#   "GeeksforGeek", "GeeksforGeeks" }
#
# Output:
# GeeksforGeeks
# User function Template for python3

class Solution:
    def longest(self, names, n):
        # code here
        len1 = 0
        x = "null"
        for i in range(n):
            if len(names[i]) > len1:
                len1 = len(names[i])
                x = names[i]
        return x


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        names = []
        for i in range(n):
            names.append(input())
        ob = Solution()
        print(ob.longest(names, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
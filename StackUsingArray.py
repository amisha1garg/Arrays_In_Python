# Write a program to implement a Stack using Array. Your task is to use the class as shown in the comments in the code editor and complete the functions push() and pop() to implement a stack.
#
# Example 1:
#
# Input:
# push(2)
# push(3)
# pop()
# push(4)
# pop()
# Output: 3, 4
# Explanation:
# push(2)    the stack will be {2}
# push(3)    the stack will be {2 3}
# pop()      poped element will be 3,
#            the stack will be {2}
# push(4)    the stack will be {2 4}
# pop()      poped element will be 4
# Example 2:
#
# Input:
# pop()
# push(4)
# push(5)
# pop()
# Output: -1, 5


# User function Template for python3

class MyStack:

    def __init__(self):
        self.arr = []

    # Function to push an integer into the stack.
    def push(self, data):
        # add code here
        # data = int(input("enter data "))
        self.arr.append(data)

    # Removes element from the stack
    def pop(self):
        # add code here
        if (len(self.arr) == 0):
            return -1
        else:
            return self.arr.pop()


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyStack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while (i < len(q1)):
            if (q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif (q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif (s.isEmpty()):
                print(-1)
                i = i + 1
        print()
        # } Driver Code Ends
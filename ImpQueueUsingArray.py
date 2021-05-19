# Implement a Queue using an Array. Queries in the Queue are of the following type:
# (i) 1 x   (a query of this type means  pushing 'x' into the queue)
# (ii) 2     (a query of this type means to pop element from queue and print the poped element)
#
# Example 1:
#
# Input:
# Q = 5
# Queries = 1 2 1 3 2 1 4 2
# Output: 2 3
# Explanation:
# In the first test case for query
# 1 2 the queue will be {2}
# 1 3 the queue will be {2 3}
# 2   poped element will be 2 the
#     queue will be {3}
# 1 4 the queue will be {3 4}
# 2   poped element will be 3

# User function Template for python3
from numpy import *


class MyQueue:
    def __init__(self):
        self.front = self.rear = 0
        self.arr = [0] * (10 ** 5)

    def push(self, x):
        self.arr[self.rear], self.rear = x, self.rear + 1

    def pop(self):
        if self.rear <= self.front: return -1
        t, self.front = self.arr[self.front], self.front + 1
        return t

    # Function to push an element x in a queue.
    # def push(self, x):

    #      #add code here
    #      return self.append(x)

    # #Function to pop an element from queue and return that element.
    # def pop(self):

    #      # add code here
    #     if len(self)==0:
    #          return -1
    #     return self.pop(self[0])


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyQueue()
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
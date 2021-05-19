# Given an array A[ ], find maximum and minimum elements from the array.
#code
T= int(input())
while(T):
    N= int(input())
    arr=list(map(int, input().split()))
    print(max(arr), min(arr),sep=" ")
    T-=1
# This is a functional problem . Your task is to return the product of array elements under a given modulo.
# The modulo operation finds the remainder after division of one number by another. For example, K(mod(m))=K%m= remainder obtained when K is divided by m.
#
# Input:
#
# The first line of input contains T denoting the number of testcases.Then each of the T lines contains a single positive integer N denotes number of element in array. Next line contain 'N' integer elements of the array.
#
#
# Output:
#
# Return the product of array elements under a given modulo.
# That is, return (Array[0]*Array[1]*Array[2]...*Array[n])%modulo.
#User function Template for python3

# arr is the array
# n is the number of element in array
# mod= modulo value
def product(arr,n,mod):
    # your code here
    x = 1
    for i in range(len(arr)):
        x = (x * arr[i]) % mod
    return x

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    mod=1000000007
    for j in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        print(product(arr,n,mod))
# } Driver Code Ends
# Given an array of integers. Check whether it contains a triplet that sums up to zero.
#
# Example 1:
#
# Input: n = 5, arr[] = {0, -1, 2, -3, 1}
# Output: true
# Explanation: 0, -1 and 1 forms a triplet
# with sum equal to 0.

// {Driver
Code
Starts
import java.util. *;

class Triplets{
public static void main(String[] args){
Scanner sc=new Scanner(System.in );
int t=sc.nextInt();


while (t -->0){
int n=sc.nextInt();
int[] a=new int[n];
for (int i=0;i < n;i++){
a[i]=sc.nextInt();
}
Solution g=new Solution();
if (g.findTriplets(a, n))
System.out.println("1");
else
System.out.println("0");

}
}
} //} Driver
Code
Ends

/ * Complete
the
function
below * /


class Solution
    {
        public
    boolean
    findTriplets(int
    a[], int
    n)
    {
        Arrays.sort(a);
    for (int i=0;i < n;i++)
    {
        int l = i+1;
    int r = n-1;
    int x = a[i];


while (l < r)
    {
    if (x + a[l] + a[r] == 0)
    {
    return true;
    }
    else if (x + a[l] + a[r] < 0)
    {
    l + +;
}
else
{
r - -;
}

}
}
return false;
}
}
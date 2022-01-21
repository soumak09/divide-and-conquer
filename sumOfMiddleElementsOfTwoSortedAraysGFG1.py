#User function Template for python3

class Solution:
    def findMidSum(self, ar1, ar2, n): 
        # code here
        arr = sorted(ar1 + ar2)
        return (arr[( len(arr)//2) - 1 ] + arr[ len(arr) // 2 ])

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":         
    tc=int(input())
    while tc > 0:
        n=int(input())
        ar1=list(map(int, input().strip().split()))
        ar2=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMidSum(ar1, ar2, n)
        print(ans)
        tc=tc-1

# } Driver Code Ends
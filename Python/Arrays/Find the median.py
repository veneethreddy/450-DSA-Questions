class Solution:
    def find_median(self, arr):
        # Code here
        arr.sort()
        if len(arr)%2==0:
            return (arr[len(arr)//2]+arr[(len(arr)//2)-1])//2
        else:
            return arr[len(arr)//2]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        v = list(map(int,input().split())) 
        ob = Solution();
        ans = ob.find_median(v)
        print(ans)
# } Driver Code Ends
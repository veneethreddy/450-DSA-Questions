class Solution:

    def rowWithMax1s(self,arr, n, m):
        # code here
        c=0
        d={}
        r=0
        s=0
        for i in arr:
            if i.count(0)==m:
                s+=1
            for j in i:
                if j==1:
                    c+=1
            d[r]=c
            r+=1
            c=0
        if s==n:
            return -1
        else:
            Keymax = max(d, key=d.get)
            return Keymax

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends
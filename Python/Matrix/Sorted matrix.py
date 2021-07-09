from itertools import islice
class Solution:
    def sortedMatrix(self,N,Mat):
        #code here
        c=[]
        for i in Mat:
            for j in i:
                c.append(j)
        c.sort()
        r=0
        l=[[0 for i in range(N)] for j in range(N) ]
        for i in range(N):
            for j in range(N):
                l[i][j]=c[r]
                r+=1
        return l        
        '''l=[N,N]
        def convert(c, l):
            res = iter(c)
            return [list(islice(res,i)) for i in l]
        res = [convert(c, l)]
        return res'''        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        v=[]
        for i in range(N):
            a=list(map(int,input().strip().split()))
            v.append(a)
        ob=Solution()
        ans=ob.sortedMatrix(N,v)
        for i in range(N):
            for j in range(N):
                print(ans[i][j],end=" ")
            print()
# } Driver Code Ends
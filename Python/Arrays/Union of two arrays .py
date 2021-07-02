class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        self.a=a
        self.n=n
        self.b=b
        self.m=m
        c=0
        s=0
        ans=[]
        ans1=[]
        for i in a:
            if i not in ans:
                ans.append(i)
            else:
                continue
        for i in b:
            if i not in ans1:
                ans1.append(i)
            else:
                continue
        for i in ans1:
            if i not in ans:
                c+=1
            else:
                continue
        for i in range(len(ans)):
            s=s+1
        return c+s    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends



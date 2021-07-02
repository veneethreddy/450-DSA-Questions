class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        self.a=a
        self.size=size
        c=0
        for i in a:
            if i<0:
                c=c+1
        if c==size:
            a.sort()
            return a[0]
        else:
            currsum=0
            maxsum=0
            for i in range(len(a)):
                currsum=currsum+a[i]
                if currsum>maxsum:
                    maxsum=currsum
                if currsum<0:
                    currsum=0
        return maxsum            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
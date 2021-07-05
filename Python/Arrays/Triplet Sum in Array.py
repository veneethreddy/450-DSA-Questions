class Solution:
    def find3Numbers(self,A, arr_size, sum):
        s = set(A)
        for i in range(0, arr_size-2):
        # Find pair in subarray A[i + 1..n-1] 
        # with sum equal to sum - A[i]
            for j in range(i + 1, arr_size-1):
                if sum-(A[i]+A[j]) in s:
                    return True
    
        return False
    


   

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,X=map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)
# } Driver Code Ends
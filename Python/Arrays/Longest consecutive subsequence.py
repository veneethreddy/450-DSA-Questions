class Solution:
    def findLongestConseqSubseq(self,arr, N):
        s = set()
        ans = 0

    # Hash all the array elements
        for ele in arr:
            s.add(ele)

    # check each possible sequence from the start
    # then update optimal length
        for i in range(n):

         # if current element is the starting
        # element of a sequence
            if (arr[i]-1) not in s:

            # Then check for next elements in the
            # sequence
                j = arr[i]
                while(j in s):
                    j += 1

            # update  optimal length if this length
            # is more
                ans = max(ans, j-arr[i])
        return ans
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

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a,n))
# } Driver Code Ends
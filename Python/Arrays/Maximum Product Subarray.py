class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self,arr, n):
        # code here
        min_arr = [1]*n

        max_arr = [1]*n

        ans = arr[0]
        min_arr[0] = max_arr[0] = arr[0]


        for i in range(1,n):
            min_arr[i] = min(arr[i],max_arr[i-1]*arr[i],min_arr[i-1]*arr[i])
            max_arr[i] = max(arr[i],max_arr[i-1]*arr[i],min_arr[i-1]*arr[i])
            ans = max(ans,max_arr[i])
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
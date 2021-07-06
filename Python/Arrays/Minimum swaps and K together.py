
def minSwap (nums, n, k) : 
    #Complete the function
    window_size=0
    for i in nums:
        window_size += 1 if i <= k else 0

        # now slide the window, check the swaps required for each window and get the min of them
    result, swaps = float('inf'), 0
    left_idx = 0

    for right_idx in range(len(nums)):
            # swap count will be increamented if the current item is greater that k
        swaps += 1 if nums[right_idx] > k else 0

            # within the window
        if right_idx - left_idx + 1 == window_size:
                # total min swaps
            result = min(result, swaps)

                # decrement swaps if the item on the left index was greater than k, as now the window will be shifted by 1
            swaps -= 1 if nums[left_idx] > k else 0
            left_idx += 1

    return 0 if result == float('inf') else result
    
    
    
    
    '''a=[]
    for i in range(n):
        if arr[i] <=k:
            a.append(arr.index(arr[i]))
            arr[i]=0
    print(a)
    c=0
    for i in range(len(a)-1):
        if a[i]+1!=a[i+1]:
            c+=1
    return c'''        



#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ans = minSwap(arr, n, k)
    print(ans)
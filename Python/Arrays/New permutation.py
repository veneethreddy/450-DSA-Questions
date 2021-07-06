class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n<=1:
            return None
        i = n-2
        j = n-1

        while(i>=0):
            if nums[i]<nums[j]:
                # find the smallest value bigger than nums[i] in nums[j:]
                for m in range(n-1,i,-1):

                    if nums[m]>nums[i]:
                        nums[m],nums[i] = nums[i],nums[m]

                        break
                nums[j:] = sorted(nums[j:])
                break
            else:
                i-=1
                j-=1
        if i == -1:
            nums.reverse()
        return None
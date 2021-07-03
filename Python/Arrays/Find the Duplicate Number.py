class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        self.nums=nums
        n = len(nums)
        for i in range(n):
            nums[nums[i]%n] += n
            
        for i in range(n):
            if nums[i]//n >= 2:
                return i
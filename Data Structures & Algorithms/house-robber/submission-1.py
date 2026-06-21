class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)

        for i in range(len(nums)-3,-1,-1):
            nums[i] = nums[i] + max(nums[i+2:])  

        return max(nums)     
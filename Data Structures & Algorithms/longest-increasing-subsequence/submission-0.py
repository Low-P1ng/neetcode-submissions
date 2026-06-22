class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        lis = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            for j in range(1,len(nums) - i):
                if nums[i]<nums[i+j]:
                    lis[i] = max(lis[i], 1 + lis[i+j])
        return max(lis)
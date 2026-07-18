class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = set()
        n = 0
        ce = nums[0]
        for i in range(len(nums)):
            if nums[i]==ce:
                n+=1
                if n>(len(nums)/3):
                    res.add(ce)
            else:
                ce = nums[i]
                n = 1
                if n>(len(nums)/3):
                    res.add(ce)
        return list(res)
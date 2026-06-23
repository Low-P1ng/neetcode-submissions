class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ds = [set([i]) for i in nums]
        ts = 0
        for elem in nums:
            ts += elem
        if ts%2!= 0: return False
        hs = ts//2
        for i in range(len(nums)-2,-1,-1):
            if nums[i] == hs: return True
            for elem in ds[i+1]:
                if elem + nums[i] == hs:
                    return True
                if elem + nums[i] < hs:
                    ds[i].add(elem+nums[i])
            ds[i].update(ds[i+1])
        return False

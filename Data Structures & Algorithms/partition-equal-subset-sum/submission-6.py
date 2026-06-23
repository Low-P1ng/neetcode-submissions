class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        possible = {0}
        ts = sum(nums)
        if ts%2: return False
        hs = ts//2
        for n in nums:
            new = set()
            for p in possible:
                if n+p == hs:
                    return True
                if n + p > hs:
                    continue
                new.add(n+p)
            possible.update(new)
        return False

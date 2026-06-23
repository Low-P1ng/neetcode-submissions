class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        possible = {0}
        ts = 0
        for elem in nums:
            ts += elem
        if ts%2!= 0: return False
        hs = ts//2
        for n in nums:
            new = set()
            for p in possible:
                if n == hs or n+p == hs:
                    return True
                if n + p > hs:
                    continue
                new.add(n+p)
            possible.update(new)
        return False

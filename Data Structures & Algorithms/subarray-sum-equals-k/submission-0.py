class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freqmap = defaultdict(int)
        freqmap[0]=1
        res = 0
        som = 0
        for i in range(len(nums)):
            som+=nums[i]
            res += freqmap[som-k]
            freqmap[som]+=1
        return res
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [ fill - empty for fill,empty in zip(gas,cost)]
        if sum(diff) < 0:
            return -1
        presum = [0] * len(diff)
        presum[-1] = diff[-1]
        for i in range(len(diff)-2,-1,-1):
            presum[i] = diff[i]+presum[i+1]
        res = 0
        for i,n in enumerate(presum):
            if n > presum[res]:
                res = i
        return res
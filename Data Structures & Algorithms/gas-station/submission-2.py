class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        petrol = 0
        res = 0
        for i in range(len(gas)):
            petrol += gas[i] - cost[i]
            if petrol < 0:
                petrol = 0
                res = i+1

        return res

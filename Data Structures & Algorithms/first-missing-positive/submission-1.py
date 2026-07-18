class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = [0]*(max(nums))
        if res:
            res.extend([0,0])
        else:
            res = [0,0]
        for elem in nums:
            if elem>0:
                res[elem] = 1

        for i in range(1,len(res)):
            if res[i] == 0:
                return i
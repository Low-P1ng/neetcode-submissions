class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, sm):
            if i == len(nums):
                if sm == target:
                    return 1
                else:
                    return 0
            
            if (i, sm) in memo:
                return memo[(i,sm)]

            memo[(i,sm)] = dfs(i+1, sm + nums[i]) + dfs(i+1, sm - nums[i])
            return memo[(i, sm)]
        return dfs(0,0)
            


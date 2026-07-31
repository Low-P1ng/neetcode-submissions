class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i,subset):
            res.append(subset.copy())

            for idx in range(i,len(nums)):
                if idx>i and nums[idx] == nums[idx-1]:
                    continue
                subset.append(nums[idx])
                dfs(idx+1,subset)
                subset.pop()

        dfs(0,[])
        return res
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        check = [False]*len(nums)
        res = []
        def dfs(check,perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i in range(len(nums)):
                if check[i] == False:
                    check[i] = True
                    perm.append(nums[i])
                    dfs(check,perm)
                    check[i] = False
                    perm.pop()

        dfs(check,[])
        return res
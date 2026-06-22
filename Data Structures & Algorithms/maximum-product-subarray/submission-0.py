class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin = curmax = 1
        for elem in nums:
            temp = curmin
            curmin = min(elem * curmin, elem * curmax, elem)
            curmax = max(elem * temp, elem * curmax, elem)
            res = max(curmax, res)
        return res
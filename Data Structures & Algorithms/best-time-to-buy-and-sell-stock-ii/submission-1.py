class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-2,-1,-1):
            res = max(res,res + prices[i+1]-prices[i])
        return res
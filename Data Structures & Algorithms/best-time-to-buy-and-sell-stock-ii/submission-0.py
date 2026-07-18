class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        maxn = prices[-1]
        for i in range(len(prices)-2,-1,-1):
            if prices[i]>maxn:
                maxn = prices[i]
                continue

            res = max(maxn - prices[i], res,res + prices[i+1]-prices[i])
        return res
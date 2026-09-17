class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        if len(prices) <= 1:
            return 0
        l, r = 0, 1
        while l < r and r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            else:
                maxProfit = max(profit, maxProfit)
            r += 1

        return maxProfit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left, right = 0, 1

        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > 0:
                maxProfit = max(profit, maxProfit)
            else:
                left = right
            right += 1

        return maxProfit
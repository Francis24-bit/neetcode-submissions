class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(1, len(prices)):
            margin = prices[i] - min(prices[:i])
            max_profit = max(max_profit, margin)
        
        return max_profit
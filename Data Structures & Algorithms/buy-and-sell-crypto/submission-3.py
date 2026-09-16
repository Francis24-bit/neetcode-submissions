class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #suppose on each day, you sell the stock.
        # you find the lowest price before that day, and get the margin, update the margin constantly.

        buy_price = prices[0]
        profit = 0
        
        for price in prices:
            if price < buy_price:
                buy_price = price
            else:
                margin = price - buy_price
                profit = max(margin, profit)
        
        return profit
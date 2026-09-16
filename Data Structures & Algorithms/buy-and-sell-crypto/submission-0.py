class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for price in prices:
            if price < buy_price:
                buy_price = price
            else:
                margin = price - buy_price
                if margin > profit:
                    profit = margin
        
        return profit
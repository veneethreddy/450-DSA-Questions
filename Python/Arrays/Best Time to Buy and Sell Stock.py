class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
            
        minPrice = float('inf')
        profit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            if price - minPrice > profit:
                profit = price - minPrice

        return profit
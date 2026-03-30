class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        B, S = 0, 1

        max_price = 0

        while S < len(prices):
            profit = prices[S] - prices[B]

            max_price = max(max_price, profit)

            if prices[B] <= prices[S]:
                S += 1
            else:
                B += 1
            
            if B == S:
                S += 1
        
        return max_price

        
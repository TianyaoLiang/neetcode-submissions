class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            profit = prices[i] - low
            max_profit = max(max_profit, profit)
        return max_profit
            
                


        
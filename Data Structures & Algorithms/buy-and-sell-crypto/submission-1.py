class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            if lowest < prices[i]:
                profit = prices[i] - lowest
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit
                


        
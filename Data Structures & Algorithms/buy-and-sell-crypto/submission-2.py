class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        max_profit = 0
        for i in range(len(prices)-1):
            if prices[i] <= low:
                low = prices[i]
            if prices[i+1] > low and prices[i+1] - low > max_profit:
                max_profit = prices[i+1] - low
        return max_profit

            

        
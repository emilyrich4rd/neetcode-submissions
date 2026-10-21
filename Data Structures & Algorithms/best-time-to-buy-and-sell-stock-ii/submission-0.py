class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for i in range(len(prices) - 1):
            change = prices[i+1] - prices[i]
            if change > 0:
                total += change
        return total

    

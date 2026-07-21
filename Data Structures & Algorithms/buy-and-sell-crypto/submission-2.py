class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0 
        p2 = 1 
        maxProf = 0 
        while p2 < len(prices):
            diff = prices[p2] - prices[p1]
            print(diff)
            if diff >= 0:
                maxProf = max(maxProf, diff)
                p2 += 1
            else:
                p1 = p2
                p2 += 1
        return maxProf
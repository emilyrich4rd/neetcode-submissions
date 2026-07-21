class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProf = 0
        for sellprice in prices:
            maxProf = max(sellprice - minBuy, maxProf)
            minBuy = min(minBuy, sellprice) # found a new buy price if our current sell price is actually lower than the old one
        return maxProf
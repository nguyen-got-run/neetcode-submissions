class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        l = 0
        
        for r in range(len(prices)):
            if l == r:
                continue

            diff = prices[r] - prices[l]
            
            if diff < 0:
                l = r
            mp = max(mp, diff)
        
        return mp
        
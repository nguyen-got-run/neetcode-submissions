class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        l = 0
        
        for r in range(len(prices)):
            if l == r:
                continue

            l_val = prices[l]
            r_val = prices[r]
            diff = r_val - l_val
            
            if diff < 0:
                l = r
            mp = max(mp, diff)
        
        return mp
        
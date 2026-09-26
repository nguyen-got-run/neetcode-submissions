class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, ans = len(prices), 0
        l, r = 0, 1

        if n < 2: return 0

        while r < n:
            buy = prices[l]
            sell = prices[r]
            profit = sell - buy

            if profit > 0:
                ans = max(ans, profit)
            else: # profit <= 0, which means we find a new low price
                l = r
            
            r += 1

        return ans
                



        
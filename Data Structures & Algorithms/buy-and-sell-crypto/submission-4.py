class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, ans = len(prices), 0

        for i in range(n):
            cur = prices[i]

            j = n - 1

            while i < j: # i=0, j=2 --> i=0, j=1 as the last case
                future = prices[j]
                profit = future - cur
                ans = max(ans, profit)
                j -= 1
        
        return ans


        
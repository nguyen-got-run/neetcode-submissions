class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans, n = 0, len(coins)
        if not amount: return ans
        
        coins.sort()
        if amount < coins[0]: return -1

        # from 0 dollar to amount dollars
        most = amount + 1
        dp = [most] * (amount + 1)
        # at 0 dollar, we need no coin change
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                left = i - coin
                if left < 0: break
                # update dp[i]: either we find a new min value, or keep the value we already computed
                # note: dp[left] is always available, because left < i (i = current money) because we're doing bottom up
                dp[i] = min(dp[i], 1 + dp[left])
                
        ans = dp[-1]
        return -1 if ans == most else ans


        
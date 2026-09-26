class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return -1
        if amount == 0: return 0

        coins.sort()
        if coins[0] > amount: return -1

        maxTimes = amount + 1 # using only 1 coins + 1
        dp = [maxTimes] * maxTimes
        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:
                diff = i - coin
                if diff < 0: break
                dp[i] = min(dp[i], 1 + dp[diff])
        
        return dp[amount] if dp[amount] != maxTimes else -1

        
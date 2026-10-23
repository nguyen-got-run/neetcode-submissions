class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans, n = 1, len(nums)
        if n == 1: return ans

        dp = [1] * n

        for i in range(1, n):
            num = nums[i]
            for j in range(i):
                prev = nums[j]
                if prev < num:
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])
        
        return ans



        
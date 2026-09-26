class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        ans = 1

        for i in range(1, n):
            curNum = nums[i]
            for j in range(0, i):
                prevNum = nums[j]
                
                if curNum > prevNum:
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])
        
        return ans
        
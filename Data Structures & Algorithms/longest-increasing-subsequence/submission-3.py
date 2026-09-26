class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        ans = 1

        for i in range(1, n):
            curNum = nums[i]
            # i think that this is ok,
            # but is there any better way?
            # for instance, we inspect 9 in [7, 8, 9]
            # then I dont think we need to go back to the 7 after visiting 8
            # but we still need to make sure it works for [7, 8, 1, 2, 3, 9]
            for j in range(0, i):
                prevNum = nums[j]
                
                if curNum > prevNum:
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])
        
        return ans
        
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        if n == 1: return nums[0]

        mi, ma = 1, 1

        for num in nums:
            tma = num * ma
            tmi = num * mi
            ma = max(tma, tmi, num)
            mi = min(tma, tmi, num)
            ans = max(ans, ma)
        
        return ans

        
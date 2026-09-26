class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        curMin, curMax, res = 1, 1, 0

        for num in nums:
            # if tmp = 0, curMax and curMin will get reset
            tmp = curMax * num
            curMax = max(tmp, curMin * num, num)
            curMin = min(tmp, curMin * num, num)

            res = max(res, curMax)
    
        return res
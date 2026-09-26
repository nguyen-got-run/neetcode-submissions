class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        # choose to rob first house
        prev0, cur0 = 0, 0
        for i in range(n-1):
            tmp = prev0 + nums[i]
            prev0 = cur0
            cur0 = max(tmp, cur0)

        # choose not to rob first house
        prev1, cur1 = 0, 0
        for i in range(1, n):
            tmp = prev1 + nums[i]
            prev1 = cur1
            cur1 = max(tmp, cur1)

        return max(cur0, cur1) 
        
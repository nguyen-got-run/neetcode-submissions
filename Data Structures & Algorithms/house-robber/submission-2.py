class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not n: return 0
        if n == 1: return nums[0]
        prev, cur = 0, nums[0]

        for i in range(1, n):
            num = nums[i]
            temp = prev
            prev = cur
            cur = max(cur, temp + num)
        
        return cur

        
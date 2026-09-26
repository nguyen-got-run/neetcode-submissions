class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, cur = 0, 0

        for num in nums:
            # skip left-adj, which is cur
            doRob = prev + num
            prev = cur
            cur = max(doRob, cur)
        
        return cur
        
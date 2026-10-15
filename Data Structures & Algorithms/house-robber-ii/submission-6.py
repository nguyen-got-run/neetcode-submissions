class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        # case 1: pick the last house, so we drop the first one 
        prev1, cur1 = 0, 0

        for i in range(1, n):
            rob = prev1 + nums[i]
            prev1 = cur1
            cur1 = max(rob, cur1)
        
        # case 2: not picking the last house, so we drop the last one
        prev2, cur2 = 0, nums[0]
        for i in range(1, n - 1):
            rob = prev2 + nums[i]
            prev2 = cur2
            cur2 = max(rob, cur2)

        return max(cur1, cur2)
        

        
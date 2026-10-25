class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        target = total // 2

        seen = set()
        seen.add(0)

        for num in nums:
            nxt = set()
            for each in seen:
                nxt.add(each)

                new = each + num
                if new == target: return True
                if new > target: continue
                nxt.add(new)
            seen = nxt
    
        return False
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        idx = -1

        while l <= r:
            m = (r + l) // 2
            val = nums[m]

            if val == target:
                idx = m
                break
            
            if val < target:
                l = m + 1
            else:
                r = m - 1

        return idx

        
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # is sorted
        if nums[0] < nums[-1]: return nums[0]
        # is not sorted
        l, r = 0, len(nums) - 1

        while l < r:

            m = (r - l) // 2 + l
            left = nums[l]
            mid = nums[m]
            right = nums[r]

            # all nums are uniq
            if mid < right: # right side is ok, check left
                r = m
            else: # right side is not ok, check right
                l = m + 1
        
        return nums[l]


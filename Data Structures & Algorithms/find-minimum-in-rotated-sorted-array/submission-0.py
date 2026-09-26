class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        # already sorted
        if nums[l] < nums[r]:
            return nums[0]
        
        minVal = nums[r]

        while l <= r:
            m = l + (r-l) // 2
            v = nums[m]

            if v > minVal:
                l = m+1
            else:
                r = m - 1
                minVal = min(minVal, v)
        
        return minVal

        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (r + l) // 2

            cur = nums[mid]
            if cur == target: return mid

            if cur > target: # too big, need to adjust right bound
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
        
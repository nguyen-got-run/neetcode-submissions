class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binsearch(l: int, r: int) -> int:
            while l <= r:
                m = (r - l) // 2 + l
                cur = nums[m]
                if cur == target: return m

                if cur > target:
                    r = m - 1
                else:
                    l = m + 1
            
            return -1
        
        if len(nums) == 1: return 0 if nums[0] == target else -1
        if nums[0] < nums[-1]: return binsearch(0,len(nums) - 1)

        l, r = 0, len(nums) - 1
        while l < r:
            m = (r - l) // 2 + l
            cur = nums[m]
            left = nums[l]
            right = nums[r]

            if left == target: return l
            if cur == target: return m
            if right == target: return r
            
            if cur > right: # left side is sorted, pivot on the right
                ans = binsearch(l, m)
                if ans >= 0: return ans
                l = m + 1
            else: # right side is sorted, pivot on the left
                ans = binsearch(m, r)
                if ans >= 0: return ans
                r = m

        return -1
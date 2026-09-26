class Solution:
    def bin_search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        i = -1

        while l <= r:
            m = (r + l) // 2
            val = nums[m]
            if val == target:
                i = m
                break
            if val < target:
                l = m + 1
            else:
                r = m -1
        
        return i

    def is_sorted(self, nums: List[int]) -> bool:
        return nums[0] <= nums[-1]

    def search(self, nums: List[int], target: int) -> int:
        if self.is_sorted(nums):
            return self.bin_search(nums, target)

        # try fo find the middle index
        # where it splits into 2 sorted sub arrays
        l = 0
        r = len(nums) - 1
        i = 0

        while l <= r:
            m = (l + r) // 2
            print(m)
            i = m
            val = nums[m]

            if val == target:
                return m
            # the left (l -> m) sub-array is already sorted
            if val >= nums[l]:
                result = self.bin_search(nums[l:m], target)
                if result >= 0:
                    return l+result
                l = m + 1
            # val < nums[l]
            else:
                r = m -1
        

        result = self.bin_search(nums[i:], target)
        if result >= 0:
            return i + result
        
        return -1



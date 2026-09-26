class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            num = nums[i]
            remainder = target - num
            m[remainder] = i
        
        print(m)
        for i in range(len(nums)):
            num = nums[i]
            if num not in m: continue
            originalIndex = m[num]
            if i == originalIndex: continue
            return [i, m[num]]

        
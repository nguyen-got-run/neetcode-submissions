class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}

        for i in range(len(nums)):
            num = nums[i]
            remainder = target - num

            if num in complement:
                return [complement[num], i]
            else: 
                complement[remainder] = i
        
        # print(complement)
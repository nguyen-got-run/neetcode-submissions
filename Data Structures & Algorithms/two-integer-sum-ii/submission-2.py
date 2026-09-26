class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            lNum = numbers[l]
            rNum = numbers[r]
            total = lNum + rNum

            if total == target:
                return [l+1, r+1]

            # too big, need smaller sum, so we move r--
            if total > target:
                r -= 1
            else: # too small, need bigger, so we move l++
                l += 1
        

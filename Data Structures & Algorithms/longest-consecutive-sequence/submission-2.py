class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set()

        for num in nums:
            numSet.add(num)
        
        longest = 1

        for num in numSet:
            toCont = True
            curLength = 1
            target = num + 1

            while toCont:
                if target in numSet:
                    target += 1
                    curLength += 1
                else:
                    toCont = False
            
            longest = max(longest, curLength)
        
        return longest

                

        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        setOfNums = set(nums)
        ans = 1

        for num in setOfNums:
            prev = num - 1
            # we should not start a sequence here
            if prev in setOfNums: continue

            consecutive = num + 1
            curCount = 1
            while consecutive in setOfNums:
                consecutive += 1
                curCount += 1
                ans = max(ans, curCount)
        
        return ans

        
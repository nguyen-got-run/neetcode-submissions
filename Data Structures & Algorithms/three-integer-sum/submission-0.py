class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        numSet = set()

        for num in nums:
            needed = target - num
            if needed in numSet:
                ans.append([num, needed])
            else:
                numSet.add(num)
        
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        targets = []
        workedPairs = set()
        ans = []
        for i in range(len(nums)):
            num = nums[i]
            numTarget = 0 - num

            pairs = self.twoSum(nums[i+1:], numTarget)
            if len(pairs):
               for pair in pairs:
                    pair.append(num)
                    smaller = min(pair)
                    bigger = max(pair)
                    key = f"{smaller}{bigger}"
                    print(key)
                    if key not in workedPairs:
                        ans.append(pair)
                        workedPairs.add(key) 
        
        return ans
        

        
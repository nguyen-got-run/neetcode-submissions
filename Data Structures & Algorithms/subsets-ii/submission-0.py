class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans, cur = [], []

        def backtrack(i):
            if i >= n:
                ans.append(cur[:])
                return

            # choose to add
            num = nums[i]
            cur.append(num)
            backtrack(i+1)
            cur.pop()
        
            # choose not to add
            toAdd = 1
            while i + toAdd < n and num == nums[i + toAdd]:
                toAdd +=1
            
            backtrack(i+toAdd)
        
        backtrack(0)

        return ans
        
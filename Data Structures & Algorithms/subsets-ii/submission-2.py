class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans, n  = [], len(nums)
        if not n: return ans

        nums.sort()

        subset = []
        def dfs(i):
            if i >= n:
                ans.append(subset[:])
                return
            
            num = nums[i]
            # choose to add nums[]
            subset.append(num)
            dfs(i + 1)
            subset.pop()

            # choose not to add num
            k = 1
            while i + k < n and num == nums[i + k]:
                k += 1
            dfs(i + k)
        
        dfs(0)

        return ans
        
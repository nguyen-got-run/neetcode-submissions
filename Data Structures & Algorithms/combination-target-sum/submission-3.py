class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, n = [], len(nums)
        if not nums: return ans

        subset = []
        def dfs(i: int, cur: int):
            if i >= n or cur > target: return
            if cur == target:
                ans.append(subset[:])
                return
            
            # choose not to continue to add i, move on to the next
            dfs(i+1, cur)

            # choose to continue to add i
            num = nums[i]
            subset.append(num)
            dfs(i, cur + num)
            subset.pop()
        
        dfs(0, 0)
        return ans
        
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        if not n: return ans

        subset = []
        def dfs(idx: int):
            if idx >= n:
                ans.append(subset[:])
                return
            
            # not to include idx
            dfs(idx+1)

            # include idx
            subset.append(nums[idx])
            dfs(idx+1)
            subset.pop() 
        
        dfs(0)
        return ans


        
        
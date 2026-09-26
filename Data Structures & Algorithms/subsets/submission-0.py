class Solution:    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sub = [], []

        def dfs(i):
            if i >= n:
                res.append(sub[:])
                return

            # choose not to add:
            dfs(i + 1)

            # choose to add
            num = nums[i]
            sub.append(num)
            dfs(i + 1)
            sub.pop()
        
        dfs(0)

        return res
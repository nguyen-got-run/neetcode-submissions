class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, n = [], len(candidates)
        
        if not n: return ans
        candidates.sort()
        
        subset = []
        def dfs(i: int, cur: int):
            if cur == target:
                ans.append(subset[:])
                return
            
            if i >= n or cur > target: return
            
            # choose to add
            c = candidates[i]
            subset.append(c)
            dfs(i + 1, cur + c)
            subset.pop()

            # choose not to i, and move to i+k where candidates[i+k] != candidates[i]
            k = 1
            while i+k < n and c == candidates[i+k]:
                k += 1
            dfs(i + k, cur)
        
        dfs(0, 0)
        return ans
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans, n = [], len(s)

        def isPalin(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True
        
        subset = []
        def dfs(i: int):
            if i == n:
                ans.append(subset[:])
                return
            
            for j in range(i, n):
                if isPalin(i, j):
                    subset.append(s[i:j+1])
                    dfs(j + 1)
                    subset.pop()
            
        dfs(0)
        return ans
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges: return 0

        adjMap = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)

        seen = set()

        def dfs(i):
            seen.add(i)
            li = adjMap[i]

            for e in li:
                if e in seen: continue
                dfs(e)

        ans = 0    
        for i in range(n):
            if i in seen: continue
            dfs(i)
            ans += 1
        
        return ans
        
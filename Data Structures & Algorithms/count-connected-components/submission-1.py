class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges: return 0

        adjMap = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)

        
        seen = set()
        ans = 0

        def dfs(i, prev):
            # if i in seen: return False

            seen.add(i)

            li = adjMap[i]

            for e in li:
                if e == prev: continue
                if e in seen: continue
                if not dfs(e, i): return False
            
            return True
        
        for i in range(n):
            if i in seen: continue
            if not dfs(i, -1): return -1

            # if len(seen) == n: return 1
            ans += 1
        
        return ans
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        nRange = range(n)
        adjMap = {i+1: set() for i in nRange}

        for n1, n2 in edges:
            adjMap[n1].add(n2)
            adjMap[n2].add(n1)
        
        ans, seen = n - 1, set()

        def dfs(i: int, prev: int) -> bool:
            if i in seen: return False
            adjLi = adjMap[i]

            seen.add(i)
            for e in adjLi:
                if e == prev: continue
                if not dfs(e, i): return False
            
            # seen.remove(i)
            return True
        
        for i in range(n-1, -1, -1):
            n1, n2 = edges[i]

            # reset seen
            seen = set()
            
            # remove from adjMap
            adjMap[n1].remove(n2)
            adjMap[n2].remove(n1)

            # dfs
            if dfs(1, -1) and len(seen) == n:
                ans = i
                break

            # add back to adjMap
            adjMap[n1].add(n2)
            adjMap[n2].add(n1)
        
        return edges[ans]
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = {i: [] for i in range(n)}
        for node1, node2 in edges:
            adjMap[node1].append(node2)
            adjMap[node2].append(node1)

        # seen is like cycle, but we dont remove n as we traverse
        # the reason if a future n already in seen
        # then that means we have a loop and hence not a valid tree
        seen = set()
        def dfs(n, prev):
            if n in seen: return False

            adjLi = adjMap[n]
            seen.add(n)
            
            for each in adjLi:
                if each == prev: continue
                if not dfs(each, n): return False
            
            return True
            
        return dfs(0, -1) and len(seen) == n
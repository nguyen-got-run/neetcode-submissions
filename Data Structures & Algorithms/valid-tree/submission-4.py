class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nRange = range(n)
        adjMap = {i: set() for i in nRange}

        for n1, n2 in edges:
            adjMap[n1].add(n2)
            adjMap[n2].add(n1)
        
        visited, seen = set(), set()
        def dfs(i: int, prev: int) -> bool:
            if i in seen: return False
            adjLi = adjMap[i]

            seen.add(i)
            for each in adjLi:
                if each == prev: continue

                if not dfs(each, i): return False
            
            visited.add(i)
            seen.remove(i)
            return True

        # at first, I was thinking that we need to do a for loop
        # because we are not sure which one is the root
        # however, since this is unidirected edges, we should be ok
        if not dfs(0, -1): return False

        return len(visited) == n

        
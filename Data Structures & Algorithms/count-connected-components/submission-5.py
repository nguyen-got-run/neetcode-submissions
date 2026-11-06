class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nRange = range(n)
        adjMap = {i: set() for i in nRange}

        for n1, n2 in edges:
            adjMap[n1].add(n2)
            adjMap[n2].add(n1)
        
        ans, visited = 0, set()
        def dfs(i: int):
            adjLi = adjMap[i]

            visited.add(i)

            for each in adjLi:
                if each in visited: continue
                dfs(each)
                        
        for i in nRange:
            if i in visited: continue
            
            # dfs to add all leaves of a connected component into visited
            dfs(i)
            ans += 1

        return ans
        
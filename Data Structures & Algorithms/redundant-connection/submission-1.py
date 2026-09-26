class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def getAdjMap(edges):
            adjMap = {}

            for n1, n2 in edges:
                if n1 not in adjMap: adjMap[n1] = []
                if n2 not in adjMap: adjMap[n2] = []

                adjMap[n1].append(n2)
                adjMap[n2].append(n1)

            return adjMap

        fullAdjMap = getAdjMap(edges)
        edges.reverse()

        for i in range(len(edges)):
            test = edges[:i] + edges[i+1:]

            adjMap = getAdjMap(test)

            seen = set()
            def dfs(n):
                seen.add(n)
                if n not in adjMap: return
                adjLi = adjMap[n]
                for e in adjLi:
                    if e in seen: continue
                    dfs(e)
            
            dfs(1)

            if len(seen) == len(fullAdjMap): return edges[i]

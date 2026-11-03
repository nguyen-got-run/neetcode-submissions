class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = {}

        for c, p in prerequisites:
            if c not in adjMap:
                adjMap[c] = set()
            adjMap[c].add(p)
    
        seen = set()

        def dfs(i: int):
            if i in seen: return False
            if i not in adjMap: return True

            adjList = adjMap[i]
            if not adjList: return True

            seen.add(i)
            for p in adjList:
                if not dfs(p): return False
            
            seen.remove(i)
            del adjMap[i]

            return True
    
        for i in range(numCourses):
            if not dfs(i): return False
        
        return True
        
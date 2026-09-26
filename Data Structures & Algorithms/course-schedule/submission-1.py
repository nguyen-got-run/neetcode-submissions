class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = {i: [] for i in range(numCourses)}
        
        # build ajdMap
        for c, p in prerequisites:
            adjMap[c].append(p)

        visited = set()
        def dfs(c):
            # base cases
            if c in visited: return False
            adjLi = adjMap[c]
            if not adjLi: return True

            visited.add(c)
            for p in adjLi:
                if not dfs(p): return False
            # we have to remove, because we're done exploring c
            # and if another un-related node has to visit c, it would not return F
            visited.remove(c)
            adjMap[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return False
        
        return True
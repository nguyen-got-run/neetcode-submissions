class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = {i: [] for i in range(numCourses)}
        
        # build ajdMap
        for c, p in prerequisites:
            adjMap[c].append(p)

        cycle = set()
        def dfs(c):
            # base cases
            if c in cycle: return False
            adjLi = adjMap[c]
            if not adjLi: return True

            cycle.add(c)
            for p in adjLi:
                if not dfs(p): return False
            # we have to remove, because we're done exploring c
            # and if another un-related node has to visit c, it would not return F
            cycle.remove(c)
            # c is good to go, which means we can treat it like it has no preqs for future uncycle node
            adjMap[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return False
        
        return True
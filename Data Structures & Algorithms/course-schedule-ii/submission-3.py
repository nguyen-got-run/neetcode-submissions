class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjMap = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            adjMap[c].append(p)

        cycle = set()
        visited = set()
        ans = []

        def dfs(c):
            if c in visited: return True
            if c in cycle: return False
            adjLi = adjMap[c]
            
            cycle.add(c)

            for each in adjLi:
                if not dfs(each): return False
            
            cycle.remove(c)
            visited.add(c)
            ans.append(c)
            
            return True

        
        for c in range(numCourses):
            if not dfs(c): return []
    
        return ans